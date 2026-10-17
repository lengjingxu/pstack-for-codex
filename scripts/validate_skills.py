#!/usr/bin/env python3
"""Validate the skill collection.

Checks every skills/<name>/SKILL.md for the Codex skill contract, the
invocation policy file, and resolvable relative links. Exits non-zero with a
report when anything fails.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)\s]+)")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    errors: list[str] = []
    names: dict[str, str] = {}

    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        rel = skill_dir.relative_to(ROOT)
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{rel}: missing SKILL.md")
            continue

        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing or malformed YAML frontmatter")
            continue

        name = fm.get("name", "")
        description = fm.get("description", "")
        if not name:
            errors.append(f"{rel}: frontmatter has no name")
        elif not NAME_RE.match(name):
            errors.append(f"{rel}: name {name!r} is not hyphen-case")
        elif name != skill_dir.name:
            errors.append(f"{rel}: name {name!r} does not match the directory")
        else:
            if name in names:
                errors.append(f"{rel}: name {name!r} already used by {names[name]}")
            names[name] = str(rel)

        if not description:
            errors.append(f"{rel}: frontmatter has no description")
        elif "</" in description or len(description) > 1024:
            errors.append(f"{rel}: description is too long or contains markup")

        policy = skill_dir / "agents" / "openai.yaml"
        if not policy.exists():
            errors.append(f"{rel}: missing agents/openai.yaml")
        elif "allow_implicit_invocation" not in policy.read_text(encoding="utf-8"):
            errors.append(f"{rel}: agents/openai.yaml sets no invocation policy")

    for md in sorted(ROOT.rglob("*.md")):
        for match in LINK_RE.finditer(md.read_text(encoding="utf-8")):
            target = match.group(1)
            if not target.startswith("."):
                continue
            path = target.split("#")[0]
            if not path:
                continue
            if not (md.parent / path).resolve().exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {target}")

    print(f"skills checked: {len(names)}")
    if errors:
        print(f"errors: {len(errors)}")
        for error in errors:
            print("  " + error)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
