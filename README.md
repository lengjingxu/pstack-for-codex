![pstack for Codex](assets/banner.svg)

# pstack for Codex

[![validate](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/lengjingxu/pstack-for-codex?style=flat-square&color=4ade80)](https://github.com/lengjingxu/pstack-for-codex/stargazers)
[![License](https://img.shields.io/github/license/lengjingxu/pstack-for-codex?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/commits/main)
[![Release](https://img.shields.io/github/v/release/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/releases)
![Status](https://img.shields.io/badge/status-early%20build-orange?style=flat-square)
![Skills](https://img.shields.io/badge/skills-55-4ade80?style=flat-square)
![Playbooks](https://img.shields.io/badge/playbooks-23-4ade80?style=flat-square)
![Principles](https://img.shields.io/badge/principles-24-4ade80?style=flat-square)

**pstack for Codex** is a Codex-native port of [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan. Same working method, same playbooks, same principles, rewired to run on Codex instead of Cursor.

[中文](README.zh-CN.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

> **TL;DR** — 55 skills, 23 playbooks, 24 principles, one routing skill. For Codex users who want agent work that is planned, verified, and evidenced. Early build, no telemetry. If you try it, tell us what changed.

## Why this port exists

Upstream pstack is built for Cursor and now ships an official Claude Code adapter. In [PR #637](https://github.com/cursor/plugins/pull/637) the maintainers added Claude Code support and explicitly dropped the Codex adapter ([commit e84046f](https://github.com/cursor/plugins/commit/e84046f96b857f4070355e491cfc4bc7759c2ba6)). Codex users were left with the method but not the wiring.

This repo keeps the author's method intact and maps the Cursor-only pieces to Codex primitives: `spawn_agent`, `$CODEX_HOME/skills`, Codex session logs, `ask_user_question`, and explicit `$poteto-mode` invocation. Where Codex has no equivalent, the skill says so and continues; it does not invent a substitute that silently changes the method.

## What's inside

**New in this port:** upstream added `/create-formal-verification-skill` in [commit 4382e68](https://github.com/cursor/plugins/commit/4382e687a50b8d2c5ce4d141d001186589cff8d5). It is ported here as `$create-formal-verification-skill`: a project-local skill that formally verifies one property where tests rarely reach, and that chooses the tool (model checker, SMT solver, proof assistant) from the question instead of prescribing one.

| Item | Count |
| --- | ---: |
| Skills | 55 |
| Playbooks | 23 |
| Principles | 24 |
| Routing skill | 1 (`$poteto-mode`) |
| Subagent prompts | 2 |
| Languages | EN, 简体中文, FR, JA, KO |

## Who it's for

- Codex users who want a repeatable engineering workflow, not a prompt pack.
- Teams that care about runtime evidence, review panels, and "not done until it runs".
- People porting pstack to another host who want a working reference.

Not for: raw model-speed benchmarks or zero-config autopilot. pstack is a workflow layer; the model still does the work.

## Early adoption and evidence

As of **2026-10-19** (repo created 2026-10-16):

| Signal | Value |
| --- | ---: |
| GitHub traffic, 14-day window | 24 unique cloners / 41 clones |
| Stars / forks / open issues | 0 / 0 / 0 |
| Releases | 1 (`v1.0.0`) |
| Commits / contributors | 4 / 1 |

What this means:

- Clones are an adoption signal, not an active-user count. CI, mirrors, and repeat clones inflate it. The repo has no telemetry and does not phone home.
- There is no public benchmark or effect data yet. We will not invent one. If you run pstack for Codex on a real task, open a [usage report](https://github.com/lengjingxu/pstack-for-codex/issues/new/choose) with the task, host, and before/after evidence.

Methodology and update log: [docs/ADOPTION.md](docs/ADOPTION.md).

## How to judge the effect

pstack does not promise a benchmark score. It changes the workflow: route the task to a playbook, require runtime evidence, verify before calling it done. To evaluate it on your repo, run the same task with and without pstack and compare:

- rework loops (how many times the agent had to restart)
- failed verification runs
- review comments and follow-up fixes
- time to merge
- diff size / files touched

Report the result; we will add it to the adoption log with your permission.

## The method, condensed

[docs/METHOD.md](docs/METHOD.md) is a one-page account of how the playbooks decide what to build: restate the problem in the agent's own words, rebuild the mental model with `$how`, `$why`, `$recall`, and `$pstack-teach`, design through prototypes and `$architect` rather than prose, and write the plan only after the design holds. It condenses the upstream author's [guide to pstack, part two](https://x.com/poteto/status/2097732320606507506) and marks where this port differs.

## Community context

These links explain why a Codex port exists and how the method is being adopted. They are context, not endorsements of this repository.

- **Upstream pstack**: [cursor/plugins](https://github.com/cursor/plugins) — 12,648 stars, 1,241 forks (2026-10-19). This is the repo that contains pstack, not this port.
- **Codex adapter dropped**: [PR #637](https://github.com/cursor/plugins/pull/637) added Claude Code support; [commit e84046f](https://github.com/cursor/plugins/commit/e84046f96b857f4070355e491cfc4bc7759c2ba6) removed the Codex adapter.
- **Community discussion**: [V2EX: "PStack officially supports Claude Code, but not Codex"](https://www.v2ex.com/t/1249647) (2026-10-17).
- **Author**: Lauren Tan ([@poteto](https://x.com/poteto)); the V2EX translation cites her post ["Coding is dead, long live Coding"](https://x.com/poteto/status/2103571281014861957).
- **Other host ports**: [pstack-codex](https://github.com/ScriptedAlchemy/pstack-codex), [pstack-muse](https://github.com/jnyross/pstack-muse), [pstack-vscode](https://github.com/hackernotfound/pstack-vscode), [opencode-pstack](https://www.npmjs.com/package/@falentio/opencode-pstack). Different hosts, same method; not endorsements.
- **X about this specific port**: no public posts found as of 2026-10-19. The X links above are upstream context. If you post about it, open an issue and we will link it.

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

Quick install:

```bash
git clone --depth 1 https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex
bash /tmp/pstack-for-codex/scripts/install.sh
```

Or copy by hand:

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

Every skill except `setup-pstack` is explicit invocation only, so installing 55 skills does not push the skill list over its context budget.

## Names that differ from upstream

- `tdd` becomes `pstack-tdd`
- `teach` becomes `pstack-teach`

Renamed because a typical Codex setup already has skills by those names, and Codex does not merge same-named skills.

## Known limits

- `make-bot-ui` drives Cursor routine webhooks. On Codex it documents the shape only and says so.
- `deslop`, `control-cli`, and `control-ui` live in Cursor's `cursor-team-kit` plugin and are not present here. The steps that use them say so and continue.
- Role models are Codex model slugs. Run `$setup-pstack` to point each role at what you actually have.
- The transcript readers expect Codex session logs at `$CODEX_HOME/sessions`.

## Verify it yourself

1. Install pstack for Codex and run `$setup-pstack`.
2. Pick a task you already know how to judge.
3. Run it once without pstack, once with `$poteto-mode`.
4. Compare the five signals above: rework, failed verification, review comments, time to merge, diff size.

Open a [usage report](https://github.com/lengjingxu/pstack-for-codex/issues/new/choose) with the result, including your Codex version and host.

## Layout

```
skills/                 55 skills, each with SKILL.md and agents/openai.yaml
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

A star helps other Codex users find it. Issues, ports to other hosts, and usage reports are all welcome. If pstack for Codex changed how your agent works, tell us what changed — that is the evidence this project needs.

## Languages

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)
