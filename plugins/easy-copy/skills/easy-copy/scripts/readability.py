#!/usr/bin/env python3
"""Grade copy for reading level. Measures it instead of guessing.

Usage:
  python3 readability.py copy.txt
  python3 readability.py copy.txt --names "Second Team,Hilltop Roasters" --target 3
  echo "Your copy here." | python3 readability.py -

Input: plain text. One line per headline, button or paragraph. Lines starting
with "#" are headlines. Blank lines are ignored.

Reading-level formulas break on very short text, so headlines and short lines
(under 8 words) are checked for length and hard words instead of a grade.
Body lines get a Flesch-Kincaid grade, and the whole body must hit --target.

Reports the Flesch-Kincaid grade for the whole piece and for each line,
sentences over the word limit, and hard words (3+ syllables) with easier
swaps from references/word-swaps.md when one exists.
Exit code 1 if the copy misses a target, so it can gate a workflow.
"""
import argparse
import re
import sys
from pathlib import Path

SWAPS_FILE = Path(__file__).resolve().parent.parent / "references" / "word-swaps.md"

# Common words that the vowel-group heuristic over-counts, or that readers
# know well enough not to flag as hard.
EASY_LONG = {
    "every", "everyone", "everything", "anyone", "anything", "already", "another",
    "customer", "customers", "family", "company", "companies", "video", "idea",
    "area", "money", "business", "businesses", "different", "important", "together",
    "remember", "tomorrow", "yesterday", "understand", "computer", "telephone",
    "invoice", "invoices", "email", "emails", "whatsapp", "online", "website",
}


def syllables(word: str) -> int:
    w = word.lower().strip("'’")
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))


def is_hard(word: str) -> bool:
    """3+ syllables, not counting -ing/-ed/-es endings (the Gunning fog rule)."""
    w = word.lower()
    if w in EASY_LONG or w == "name" or syllables(w) < 3:
        return False
    for suffix in ("ing", "ed", "es"):
        if w.endswith(suffix) and syllables(w[: -len(suffix)]) < 3:
            return False
    return True


def load_swaps() -> dict:
    swaps = {}
    if SWAPS_FILE.exists():
        for line in SWAPS_FILE.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if m and m.group(1).lower() not in ("hard", "---", "instead of"):
                for hard in m.group(1).split(","):
                    swaps[hard.strip().lower()] = m.group(2).strip()
    return swaps


def strip_names(text: str, names: list) -> str:
    for n in sorted(names, key=len, reverse=True):
        if n:
            text = re.sub(re.escape(n), "Name", text, flags=re.IGNORECASE)
    return text


def split_sentences(text: str) -> list:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if re.search(r"[A-Za-z]", p)]


def words_of(text: str) -> list:
    text = re.sub(r"[$€£]?\d[\d,.%]*[a-zA-Z]{0,2}", "", text)  # numbers, money, 45%
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", text)


def fk(words: list, sentences: int) -> float:
    if not words or not sentences:
        return 0.0
    syl = sum(syllables(w) for w in words)
    return 0.39 * (len(words) / sentences) + 11.8 * (syl / len(words)) - 15.59


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="text file, or - for stdin")
    ap.add_argument("--target", type=float, default=3.0, help="max grade for the body copy as a whole (default 3 = third grade)")
    ap.add_argument("--line-target", type=float, default=5.0, help="max grade for any single body line (default 5)")
    ap.add_argument("--max-words", type=int, default=15, help="max words per sentence (default 15)")
    ap.add_argument("--names", default="", help="comma-separated brand, product and example names to ignore")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8")
    names = [n.strip() for n in args.names.split(",") if n.strip()]
    swaps = load_swaps()

    all_words, all_sents, fails, hard_found = [], 0, [], {}
    print(f"{'grade':>6}  line   ('short' = too short to grade; checked for length and hard words)")
    for line in raw.splitlines():
        if not line.strip():
            continue
        is_head = line.lstrip().startswith("#")
        text = strip_names(line.lstrip("# ").strip(), names)
        sents = split_sentences(text) or [text]
        words = words_of(text)
        if not words:
            continue
        hard_here = [w for w in words if is_hard(w)]
        if is_head or len(words) < 8:
            problems = []
            if is_head and len(words) > 10:
                problems.append(f"{len(words)} words (max 10 for a headline)")
            if hard_here:
                problems.append("hard words: " + ", ".join(hard_here))
            flag = " <- " + "; ".join(problems) if problems else ""
            if problems:
                fails.append(f"{'Headline' if is_head else 'Short line'} {'; '.join(problems)}: {line.strip()[:80]}")
            print(f"{'short':>6}  {line.strip()[:100]}{flag}")
        else:
            grade = fk(words, len(sents))
            all_words += words
            all_sents += len(sents)
            flag = " <- too hard" if grade > args.line_target else ""
            if flag:
                fails.append(f"Line at grade {grade:.1f} (max {args.line_target:g}): {line.strip()[:80]}")
            print(f"{grade:6.1f}  {line.strip()[:100]}{flag}")
        for s in sents:
            n = len(words_of(s))
            if n > args.max_words:
                fails.append(f"Sentence has {n} words (max {args.max_words}): {s[:80]}")
        for w in hard_here:
            hard_found[w.lower()] = hard_found.get(w.lower(), 0) + 1

    overall = fk(all_words, all_sents)
    hard_pct = 100 * sum(hard_found.values()) / max(1, len(all_words))
    print(f"\nBody grade: {overall:.1f} (target {args.target:g} or lower)")
    print(f"Words: {len(all_words)}  Sentences: {all_sents}  Avg words/sentence: {len(all_words) / max(1, all_sents):.1f}")
    print(f"Hard words (3+ syllables): {hard_pct:.0f}% (aim for under 10%)")
    if overall > args.target:
        fails.insert(0, f"Body grade {overall:.1f} is above target {args.target:g}")
    if hard_pct >= 10:
        fails.append(f"Hard words are {hard_pct:.0f}% of the copy (aim for under 10%)")
    if hard_found:
        print("\nHard words to check:")
        for w, c in sorted(hard_found.items(), key=lambda x: -x[1]):
            tip = f"  -> try: {swaps[w]}" if w in swaps else ""
            print(f"  {w} ({c}){tip}")
    if fails:
        print("\nFix before shipping:")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("\nPasses.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
