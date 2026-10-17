# Contributing

Issues and pull requests are welcome.

## What belongs here

This repository ports pstack to Codex. The method belongs to the upstream project, so changes here stay inside the port's scope:

- Host wiring: tool names, paths, config locations, invocation policy.
- Mapping corrections: a Cursor feature that maps to a Codex primitive more accurately than it does today.
- Guide prose that still describes Cursor behavior rather than Codex.

A change to the method itself, such as a new playbook or a rewritten principle, belongs upstream in [cursor/plugins](https://github.com/cursor/plugins). Open it there so every host benefits, and this repository will pick it up.

## Before you open a pull request

```bash
python3 scripts/validate_skills.py
```

CI runs the same check on every push and pull request. It verifies the frontmatter contract, that each skill name matches its directory name, the presence of the invocation policy file, duplicate names, and that every relative link resolves.

## Keeping up with upstream

Re-apply the mapping after an upstream change, then rerun the validator. The mapping table in the README is the checklist.
