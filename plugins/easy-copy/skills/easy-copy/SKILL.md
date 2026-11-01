---
name: easy-copy
description: "Write website and marketing copy that anyone gets on the first read. Use when AI-written copy sounds technical, wordy or robotic, or when someone says \"I had to read it twice\". Write, rewrite or review any marketing or product copy so it reads at a third-grade level, lands on the first read and gets the reader to act. Outcome-led, benefit-led and conversion-focused, and always run through the no-ai-slop skill. Use for every copywriting task, for any brand: websites, landing pages, headlines, hero sections, features, FAQs, CTAs, emails, ads, social posts, sales pages and in-app text. Also use when someone says copy is confusing, too clever, too wordy, jargon-heavy or \"I had to read it twice\". Style reference is outrank.so and squad.so."
---

# Easy Copy

Copy that a busy, non-technical reader gets on the first read, and that makes them act.

Three rules decide every word:
1. **Third-grade easy.** Short words. Short sentences. One idea at a time. Measured with a script, not guessed.
2. **Outcome first.** Say what the reader gets, then how. Every line earns a "so what?"
3. **No AI slop.** Every draft goes through the `no-ai-slop` skill before you hand it over.

This came from a real test. A business owner, the exact reader the site was for, only understood a website after he looked at its example graphics. The fix was a set of habits, the same ones outrank.so and squad.so use.

## Step 0. Load no-ai-slop (every time)

This skill depends on Peter Yang's `no-ai-slop` skill (https://github.com/petergyang/no-ai-slop). Check it before writing:

1. If available as an installed skill, read and follow it and its `eval.md`.
2. Otherwise, load both source files for this session with a supported read or web tool:
   - https://raw.githubusercontent.com/petergyang/no-ai-slop/main/skills/no-ai-slop/SKILL.md
   - https://raw.githubusercontent.com/petergyang/no-ai-slop/main/skills/no-ai-slop/eval.md
3. Installing a dependency is a separate action. Do not run a global installer just because this skill mentions it. Use the host's supported skill-management flow only when authorized.
4. If either required file cannot be read, stop and explain the blocker before writing copy. Don't claim a pass from memory.

Never skip the slop pass. Loading the files for this session meets the dependency; it does not mean the skill was installed.

## Step 1. Collect the inputs

Get these from the brief, the project's product or brand context file, or a connected business-context source. If something is missing, ask for all of it in one short list:

- **Product:** what it is, what it does, and what's live versus planned.
- **Reader:** who they are, how technical they are, and the exact words they use for their problem.
- **Segments:** two or three groups the reader would recognise themselves in.
- **Outcome:** the one result the reader wants most.
- **Proof:** real results, numbers or quotes. "None yet" is a valid answer.
- **Objections:** why they'd say no (price, setup, fit, trust, timing).
- **Constraints:** banned words, voice, currency, region, and what must stay internal.
- **Format and goal:** web page, email, ad and so on, plus the one action the reader should take.

The context source wins on facts. This skill sets the form. Preserve the brand's tone, audience and offer. Plain language does not require a SaaS voice: for a service, say what the people do. Do not invent automation, free trials, guarantees, fixed setup times or results to fill a formula.

For a reference-site review, read all existing references before calling a technique missing. Distinguish a new technique from an existing rule with a fresh example. Use `references/reference-patterns.md` for the additional patterns observed on Squad and Outrank, plus adaptation and evidence checks.

## Step 2. Plan before you write

- **Benefit ladder.** For each feature, climb from feature to benefit to outcome to feeling. Headlines use the outcome, body copy uses the benefit, and the feature becomes a short proof line. See `references/conversion.md` §1.
- **Examples bank.** Write one concrete case per segment, with realistic business names and the same numbers everywhere. See `references/formulas.md`, "Examples bank".
- **Reader's words.** List 5 to 10 phrases the reader actually says, and use them.
- **Objections.** Pick the top five and decide where each one gets answered.
- **Frame.** Pick PAS, BAB, AIDA or 4Ps for the page or section. See `references/conversion.md` §2.
- **Promise and proof map.** For each main promise, note the delivered output, the steps that produce it, the reader's role, and the evidence. Keep an output the provider controls separate from a result that depends on others. See `references/reference-patterns.md`.

## Step 3. Draft with the formulas

- **Structure.** Follow the page skeleton and formulas in `references/formulas.md`: hero, problem, jobs, the output, how it works, a day or first month with it, trust, who it's for, proof, FAQ and final CTA. For other page types (one page per job, pricing, comparison, case study, About, testimonials), use `references/page-types.md`.
- **Headlines.** Write 10 options for the main headline, score them on the 4 U's (useful, urgent, unique, ultra-specific), and pick one. Keep the next two as test variants.
- **Features.** Name each one as a job the product does ("Invoice chaser"), with one line on what it does.
- **First screen.** It must say what it is, who it's for, what you get, and what to do next. See `references/conversion.md` §4.
- **Buttons.** Each one says what happens ("Get my free audit"), with true risk reducers next to it.
- **Show, don't describe.** Put the real output on the page, word for word: the email, list or report the product makes, labelled as an example. For a complex offer, show one complete path from request through work to output and the reader's next step. Keep one case and its facts consistent throughout.
- **Make control visible.** Put the review, edit, approve or handoff step beside the relevant claim or example. Use only controls the offer actually includes. A broad trust slogan is not a substitute for saying who does what.
- **Effort and limits.** Give a verified setup time if known; otherwise say what the reader must do. Say what the offer won't do ("It doesn't move money").

## Step 4. Make it third-grade easy

Rewrite until all of these are true:

- **Short sentences.** Aim for 8–12 words. Never more than 15.
- **Short words.** Use one or two syllables when you can. Swap hard words using `references/word-swaps.md`. Keep a longer word only if it's the reader's own word ("invoice", "contract").
- **One idea per sentence.** Split at "and", "which" and "so that".
- **The product is the subject, with an everyday verb:** reads, finds, writes, sends, reminds, shows.
- **Active voice:** "It writes the message", not "The message is written".
- **Concrete over abstract:** names, numbers, days and things you can picture.
- **You and your:** talk to the reader.
- **No metaphors in headlines.** "Your customer list is leaking money" fails. "Find the customers who stopped buying" passes.
- **Explain before you name.** "A free check of your invoices, called a Revenue Audit." Never use an internal name as a headline on its own.
- **No trade words:** B2B, churn, cross-sell, ROI, optimize, leverage. Use the plain phrase from the word-swaps table.

Then measure it. Put the copy in a text file with one line per headline or paragraph, and start each headline with `#`. Then run:

```sh
python3 scripts/readability.py copy.txt --names "Brand Name,Example Co"
```

- **Target:** body grade 3 or lower. No line above grade 5. Headlines 10 words or fewer, with no hard words. Under 10% hard words overall.
- Pass brand, product and example names in `--names` so they don't count against the score.
- Fix everything listed under "Fix before shipping" and run it again until it passes.
- If you have no shell, check by hand: count the words per sentence and look for words of three or more syllables. Report it as a manual check, never a measured grade.
- Report the script's result as an estimate, with the names excluded. Its hard-word numerator includes short lines and headings, while its denominator includes only graded body lines; do not call that percentage a whole-copy measure. Names become one token and numbers are stripped. Check the original sentence lengths by hand too. Do not split one sentence across lines to game the score.

## Step 4b. Check that shorter is still true

Cutting words can quietly change the meaning. After you shorten anything, put each new line next to the long version it replaced. Check four things:

1. **Who does it.** The same person or thing must still do the action. "Suggests replies" is not "replies for you". "Writes a message for you to send" is not "messages your customers".
2. **What's included.** No part of the offer can drop out. "Free returns on shoes and bags" is not "free returns".
3. **How strong the claim is.** The promise can't get bigger. "Helps you" is not "gets you", and "can" is not "will".
4. **Limits and conditions.** Keep words like "up to", "from", "over $50", "for 14 days" and "most". "Free shipping on orders over $50" is not "free shipping".

| Check | Long, true | Short, now wrong |
| --- | --- | --- |
| Who does it | Prepares your tax return for you to check and file | Files your taxes |
| What's included | Win back customers or collect unpaid invoices | Win back customers |
| How strong | Helps you sleep better | Fixes your sleep |
| Limits | Free shipping on orders over $50 | Free shipping |

If any check fails, put the words back or find a different short version. Being clear never justifies a line that's no longer true.

## Step 5. Run the no-ai-slop pass

1. **Detect.** Run `no-ai-slop` in detect mode on the whole draft and fix every pattern it names: binary contrasts, colon reveals, dramatic fragments, fake-profound endings, puffery, and so on.
2. **Edit.** Run its edit pass and check the result against its `eval.md`.
3. **Settle conflicts.** If no-ai-slop and this skill disagree, keep the meaning and the third-grade level. Then fix the slop pattern another way. Example: no-ai-slop says "don't dumb it down". Here, simpler words are the goal, but you still keep every fact and the precision.
4. **Re-check the reading level and the meaning.** Run `readability.py` again, because edits often make sentences longer. Run the Step 4b check on anything the slop pass shortened.

## Step 6. Final tests

- **The Jayson test.** Imagine a busy owner who isn't technical and won't look at the pictures. Does every line make sense from the text alone?
- **The skim test.** Do the headline, the line under it and each section heading say what it is, who it's for and what you get?
- **The say-it-aloud test.** Would the reader say this sentence to a friend? Read it out loud and rewrite anything you stumble on.
- **The so-what test.** Does every claim end in something the reader gets?
- **The honesty test.**
  - No invented stats, testimonials, logos or urgency.
  - Nothing unbuilt is shown as live.
  - Example names are labelled as examples.
  - A demo shows how the offer works; it does not prove a customer result.
  - Claims agree across the hero, examples, pricing, FAQ and final CTA. Reconcile conflicts from the product source before shipping.
  - Borrowed techniques are hypotheses to test, not evidence of higher conversion.

## Step 7. Hand it over

Return:
1. **The final copy**, in page order, ready to paste.
2. **Two headline variants** to A/B test.
3. **The readability result:** body grade, the longest sentence, and the hard-word percentage.
4. **A short "What changed" list**, one line per change. For a rewrite, give a before/after table of the headlines.

## Final checklist

- [ ] no-ai-slop was installed (or loaded from GitHub for this session), and the draft passed both its detect and edit passes.
- [ ] The body reads at grade 3 or lower, no sentence is over 15 words, and every headline is 10 words or fewer with no hard words.
- [ ] The headline states an outcome the reader wants, with no metaphor.
- [ ] The line under the headline says what it is and does, with the product as the subject.
- [ ] The first screen answers what, who, what I get and what to do next.
- [ ] The copy has at least one concrete example per segment.
- [ ] Features are named as jobs, each with one line on what it does.
- [ ] The page shows the real output (an email, list or report), not just a description of it.
- [ ] The copy says how much effort setup takes and what the product won't do.
- [ ] There is one goal per page, and each button says what happens, with true risk reducers next to it.
- [ ] The top objections are answered where they come up.
- [ ] All proof is real. If there's none, the page says what's honestly true.
- [ ] Each major promise has a clear mechanism, deliverable, reader role and fitting evidence.
- [ ] Output, business result and illustrative demo are not presented as interchangeable proof.
- [ ] The page fits this brand and offer; no borrowed feature, guarantee or unsupported timeline was added.
- [ ] Example names sound real, are labelled, and use the same numbers everywhere.
- [ ] Every shortened line passes the Step 4b check: it has the same doer, the same scope, a claim no stronger than before, and the same limits.
- [ ] Meta tags, share images and any AI-readable files (llms.txt) match the new copy.
