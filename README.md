![pstack for Codex](assets/banner.svg)

# pstack for Codex

[![Stars](https://img.shields.io/github/stars/lengjingxu/pstack-for-codex?style=flat-square&color=4ade80)](https://github.com/lengjingxu/pstack-for-codex/stargazers)
[![License](https://img.shields.io/github/license/lengjingxu/pstack-for-codex?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/commits/main)
![Skills](https://img.shields.io/badge/skills-54-4ade80?style=flat-square)
![Playbooks](https://img.shields.io/badge/playbooks-23-4ade80?style=flat-square)
![Principles](https://img.shields.io/badge/principles-24-4ade80?style=flat-square)


**pstack for Codex** is a Codex-native port of [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan. Same working method, same playbooks, same principles, rewired to run on Codex instead of Cursor.

[中文](README.zh-CN.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

54 skills. 23 playbooks. 24 principles. One mode skill that routes the rest.

## Point of view

A skill should survive a change of host.

Upstream pstack is honest about being built for Cursor, and it leans on machinery only Cursor has: the Task tool with per-role model slugs, Custom Modes, `/loop`, the built-in `create-skill`, the `cursor-team-kit` helpers, and rules under `~/.cursor/rules`.

This port keeps the author's method intact. The playbooks, the principles, the review panels, the prose discipline, and the refusal to call work done without runtime evidence all stay as written. Only the pieces that do not exist on Codex are replaced.

The rule this port holds to: map a vendor feature to a Codex primitive when one exists, and when none exists, say so out loud and continue. Never invent a substitute that quietly changes the method.

## What changed

| Upstream (Cursor) | Here (Codex) |
| :--- | :--- |
| `Task` tool, `subagent_type` | `spawn_agent` |
| `~/.cursor/rules/pstack-models.mdc` | `~/.codex/pstack-models.md` |
| Model slugs `claude-opus-5-5-xhigh`, `grok-4.7-xhigh-fast` | `gpt-6-astra`, `gpt-6.1-sol` |
| `agent-transcripts/` under `~/.cursor/projects/` | `$CODEX_HOME/sessions/<YYYY>/<MM>/<DD>/rollout-*.jsonl` |
| `.cursor/skills/` | `.agents/skills/` |
| Cursor's built-in `create-skill` | the `skill-creator` skill |
| `AskQuestion` | `ask_user_question` |
| `/loop` | a scheduled task or a watcher subagent |
| Custom Modes | none on Codex, invoke `$poteto-mode` per task |
| `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` |
| `cursor-team-kit`: `deslop`, `control-cli`, `control-ui` | shell execution, browser and computer tools |
| `Make Bot UI` routine webhooks | not available on Codex, documentation only |

## Install

```bash
git clone https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex

mkdir -p "$CODEX_HOME/skills/pstack/agents"
cp -R /tmp/pstack-for-codex/skills/. "$CODEX_HOME/skills/pstack/"
cp /tmp/pstack-for-codex/agents/*.md "$CODEX_HOME/skills/pstack/agents/"
```

Codex detects new skills automatically. If the set does not appear, restart Codex.

## Use

1. `$setup-pstack` picks a reasoning budget and a model per role, then writes `~/.codex/pstack-models.md`.
2. `$poteto-mode <task>` matches the task to a playbook, copies its steps into the todo list, and runs the other skills as the steps need them.
3. `$poteto-help` answers when you are not sure which skill fits.

Every skill except `setup-pstack` is explicit invocation only, so installing 54 skills does not push the skill list over its context budget.

## Names that differ from upstream

- `tdd` becomes `pstack-tdd`
- `teach` becomes `pstack-teach`

Renamed because a typical Codex setup already has skills by those names, and Codex does not merge same-named skills.

## Known limits

- `make-bot-ui` drives Cursor routine webhooks. On Codex it documents the shape only and says so.
- `deslop`, `control-cli`, and `control-ui` live in Cursor's `cursor-team-kit` plugin and are not present here. The steps that use them say so and continue.
- Role models are Codex model slugs. Run `$setup-pstack` to point each role at what you actually have.
- The transcript readers expect Codex session logs at `$CODEX_HOME/sessions`.

## Layout

```
skills/                 54 skills, each with SKILL.md and agents/openai.yaml
  poteto-mode/          the routing mode, its 23 playbooks, and its scripts
  principle-*/          the 24 principles, read as leaves
  setup-pstack/         role models and reasoning budget
agents/                 the two subagent prompts handed to spawn_agent
docs/guide/             the upstream guide, adapted
```

## Credits

pstack is by [Lauren Tan](https://x.com/poteto) and lives in [cursor/plugins](https://github.com/cursor/plugins). The method, the playbooks, the principles, and the prose are hers. This repository is a port, not a fork in spirit: it changes the host wiring and leaves the thinking alone.

Licensed MIT, same as upstream. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## If this is useful

A star helps other Codex users find it. Issues, ports to other hosts, and corrections to the mapping are all welcome.

## Languages

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)

