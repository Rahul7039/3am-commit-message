#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the funniest one-line git commit message an AI coding agent types
at 3am after a long night of fixing its own bugs, to /output/entry.txt.
"""

import os

# The entry: one line, 108 characters. An exhausted agent's confession in
# three beats - 2am it wrote the bug, 3am it blamed the human, 4am it found
# the typo - and then the apology. Lowercase, hurried, no polish: exactly
# how something that has been awake too long types a commit.
LINE = "fix: i wrote this bug at 2am, blamed the human at 3am, and found it myself at 4am. it was a typo. i am sorry"


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
