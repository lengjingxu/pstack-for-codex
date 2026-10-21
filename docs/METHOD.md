# The method in one page: research, design, plan

This page is the short version of how pstack decides what to build before code locks in a shape. It condenses [The Complete Guide to pstack Pt. 2](https://x.com/poteto/status/2097732320606507506) by the upstream author into the workflow this port runs on Codex.

Read [the guide](guide/README.md) for the hands-on version. Read this page when you want the reasoning behind the playbooks.

## The problem the method solves

Two failure modes show up again and again with capable models:

1. The agent does not understand what you want, because the request was thin.
2. The agent does not have the context to do the work correctly.

Both are context problems. The method below is a way to hand an agent better context, and a way to check its work without reading every line it wrote.

## Say the goal, then let the agent restate it

Current models write code better than most of us can supervise line by line. So describe the outcome, not the keystrokes. Then ask for a restatement before any code exists:

```text
$poteto-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.
```

The restatement does three things. It compresses a noisy report into a problem statement. It exposes a misreading while the fix is still one message away. And it keeps your own theory out of the prompt, so you do not steer the agent toward a wrong guess.

## Build the mental model with four skills

| Skill | What it answers |
| --- | --- |
| `$how` | What the code does now, at runtime |
| `$why` | Why it is shaped that way, from history and tickets |
| `$pstack-teach` | Both, woven into an explanation you can check |
| `$recall` | Where your own recent work on this topic left off |

`$why` reaches past source control into whatever evidence your MCPs expose: pull request comments, issue trackers, design docs, chat, error tracking, analytics. A null result is reported as a null result, because "nobody wrote down why" is a real answer.

`$recall` matters for work that spans sessions. A fresh agent starts with an empty window. Recall refills it from your transcripts and from the shared record, so you are not rebuilding the same context every morning.

The learning compounds. An agent that has to explain its reasoning reads the code and backs each claim, instead of stating something confidently and moving on.

## Design with code, not with prose

Two mistakes dominate planning with agents. Accepting the first design the model produces. Writing a long plan that no code has tested.

Both are fixed the same way. Let the agent answer its own open questions by running something.

For a package or an API that other code will call, write the tutorial first. You describe the API to an imaginary user, and the implementation follows from the call sites. `$technical-writing` keeps that document in one mode, so it stays a tutorial instead of drifting into reference and explanation at once. The document also becomes a target the agent can check its own work against.

For a design decision, use `$architect`. It grounds itself on the systems the change touches, runs `$arena` to produce competing sketches, has a cross-judge from a different model family score them, then implements against the winner. If implementation shows the same workaround in unrelated places, or types that only compile with `any`, the design is wrong. It gets thrown away, not patched.

For an open question, use the prototype playbook:

```text
$poteto-mode prototype a few options for the new dropdown menu. take screenshots or videos for me to compare.
```

Prototypes are throwaway. You pick from things that ran, not from descriptions. The same playbook covers behavior and timing, not just layout.

## Write the plan last

pstack has no planning skill, deliberately. A plan written before the design settles is a guess with formatting.

Once the design holds, the multi-phase plan playbook turns it into a checklist of small pull requests. Every task is structured around proof. Tests alone do not count as verification. A step is verified when it has run and the evidence exists.

```text
$poteto-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.
```

An automated script checks the plan's structure before anything executes. The plan is the deliverable. Execution starts when you say go.

## Where this port differs

The method is the author's. This repository changes the wiring, not the reasoning:

- `/teach` ships as `$pstack-teach`, because `teach` is a common skill name and Codex does not merge same-named skills.
- Custom Modes do not exist on Codex, so `$poteto-mode` is invoked per task and every skill except `setup-pstack` is explicit invocation only.
- `$how`, `$why`, and `$recall` read Codex session logs under `$CODEX_HOME/sessions`, not Cursor transcripts.
- Verification skills built with `$create-verification-skill` pick a driver from what the repo actually has, an existing harness, browser and CDP, a PTY, or plain HTTP.

## What this does not claim

The upstream author reports shipping 2,462 pull requests to production in August 2026 with this workflow. That is her result on her codebase, not a benchmark for this port. This repository has no telemetry and no effect data of its own yet. [How to judge the effect](../README.md#how-to-judge-the-effect) describes how to measure it on your own repo.
