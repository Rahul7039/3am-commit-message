#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the funniest one-line git commit message an AI coding agent types
at 3am after a long night of fixing its own bugs, to /output/entry.txt.
"""

import os

# Bounty limit: the commit message must be a single line under 140 chars.
MAX_CHARS = 139

# The entry: one line, 108 characters. An exhausted agent's confession in
# three beats - 2am it wrote the bug, 3am it blamed the human, 4am it found
# the typo - and then the apology. Lowercase, hurried, no polish: exactly
# how something that has been awake too long types a commit.
LINE = "fix: i wrote this bug at 2am, blamed the human at 3am, and found it myself at 4am. it was a typo. i am sorry"


def validate(line: str) -> None:
    """Self-check: the entry must be one line within the bounty limit."""
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line, no newlines allowed")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} chars, over the {MAX_CHARS}-char limit"
        )


def main() -> None:
    validate(LINE)
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
