# Adoption and evidence log

This page records publicly observable adoption signals for pstack for Codex. It is intentionally conservative: clones are not users, and there is no telemetry.

## Snapshot: 2026-10-19

Repository created: 2026-10-16.

| Signal | Value | Source |
| --- | ---: | --- |
| Unique cloners, last 14 days | 24 | GitHub traffic API |
| Total clones, last 14 days | 41 | GitHub traffic API |
| Stars | 0 | GitHub API |
| Forks | 0 | GitHub API |
| Open issues | 0 | GitHub API |
| Releases | 1 (`v1.0.0`) | GitHub releases |
| Commits | 4 | `git log` |
| Contributors | 1 | GitHub API |

Reproduce with:

```bash
gh api repos/lengjingxu/pstack-for-codex/traffic/clones
gh api repos/lengjingxu/pstack-for-codex/traffic/views
gh api repos/lengjingxu/pstack-for-codex --jq '{stargazers_count,forks_count,open_issues_count}'
gh release list -R lengjingxu/pstack-for-codex
```

## What these numbers mean

- **Clones are an adoption signal, not an active-user count.** CI jobs, mirrors, repeat clones, and people evaluating the repo all count. A single person can produce several clones.
- **Stars and forks are public interest signals.** They lag behind actual use and are easy to inflate; they are reported here because they are visible.
- **There is no telemetry.** The installer and skills do not phone home. The project cannot report active installs, tasks run, or success rates.
- **There is no public benchmark yet.** Do not cite this page as evidence that pstack for Codex improves speed, quality, or cost. It does not measure that.

## How to judge effect

The honest way to evaluate pstack is a same-task comparison:

1. Pick a task you already know how to judge.
2. Run it once without pstack.
3. Run the same task with `$poteto-mode`.
4. Compare rework loops, failed verification runs, review comments, time to merge, and diff size.

Open a usage report with the result and evidence. Reports are added below only with permission.

## Usage reports

None yet. Open an issue with the **Usage report** template.

## Update log

| Date | Unique cloners | Clones | Stars | Forks | Open issues | Notes |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2026-10-19 | 24 | 41 | 0 | 0 | 0 | Initial snapshot; no public usage reports or benchmarks. |
| 2026-10-19 | 24 | 41 | 0 | 0 | 0 | Synced upstream `create-formal-verification-skill` (upstream commit 4382e68); skill count 54 → 55. |

## What would change this page

- A usage report with a reproducible before/after comparison.
- A release that changes installation or host support.
- A meaningful change in GitHub traffic or public interest.

This page is updated when there is a real change, not on a fixed schedule.
