# Third-party notices

## pstack

This repository is a port of pstack.

- Source: https://github.com/cursor/plugins/tree/main/pstack
- Part of: https://github.com/cursor/plugins
- Author: Lauren Tan (https://x.com/poteto)
- License: MIT
- Version ported: 0.15.25

The skills, playbooks, principles, agent prompts, scripts, and guide pages in `skills/`, `agents/`, and `docs/` originate from pstack. The upstream LICENSE is kept verbatim at [LICENSE](LICENSE).

What this repository changed:

- Tool and path references, from the Cursor equivalents to the Codex equivalents listed in the README.
- Model role slugs, from the Cursor model names to Codex model names.
- Skill frontmatter, from Cursor keys to the Codex skill schema plus `agents/openai.yaml`.
- Two skill names, `tdd` and `teach`, renamed to `pstack-tdd` and `pstack-teach` to avoid collisions.
- Guide prose, where it described Cursor-only behavior.

What this repository did not change:

- The method, the playbooks, the principles, the review panels, and the writing discipline.
- The upstream LICENSE.

