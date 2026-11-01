# easy-copy

A Claude plugin marketplace with one plugin, **easy-copy**. It writes, rewrites and reviews website and marketing copy so a busy, non-technical reader gets it on the first read and acts on it.

The skill makes copy:

- **Third-grade easy.** Uses short words, short sentences and one idea at a time. A bundled script measures the reading level, so nobody has to guess.
- **Outcome first.** Says what the reader gets before it says how.
- **Free of AI slop.** Runs every draft through Peter Yang's [`no-ai-slop`](https://github.com/petergyang/no-ai-slop) skill before it hands the copy over.

Use it for landing pages, hero sections, features, FAQs, CTAs, emails, ads, social posts, sales pages and in-app text.

## Install

### claude.ai and Cowork

1. Open **Customize → Plugins** in your account, or **Organization settings → Plugins** to add it for your whole org.
2. Add a marketplace from GitHub and enter `adrianchinghc/easy-copy`.
3. Install **easy-copy**. claude.ai syncs the plugin to Claude Code for you as well.

If the repository is private, the Claude GitHub App needs access to it.

### Claude Code

```bash
claude plugin marketplace add adrianchinghc/easy-copy
```

```bash
claude plugin install easy-copy@easy-copy
```

Then ask for copy as usual, or call the skill directly with `/easy-copy:easy-copy`.

## Layout

```
.claude-plugin/marketplace.json        marketplace catalog
plugins/easy-copy/
  .claude-plugin/plugin.json           plugin manifest (bump "version" to ship updates)
  .claude-plugin/icon.png              listing icon
  skills/easy-copy/
    SKILL.md                           the skill
    references/                        formulas, word swaps, conversion and page-type guides
    scripts/readability.py             reading-level checker
    assets/icon.svg
    agents/openai.yaml                 metadata for OpenAI/Codex hosts
```

## Ship an update

1. Edit files under `plugins/easy-copy/`.
2. Bump `version` in `plugins/easy-copy/.claude-plugin/plugin.json`. Installed copies only update when the version changes.
3. Run `claude plugin validate .` and push to `main`.

## Add another plugin

Create `plugins/<name>/` with its own `.claude-plugin/plugin.json` and `skills/`. Then add an entry to the `plugins` array in `.claude-plugin/marketplace.json` whose `name` matches the plugin's manifest `name`.
