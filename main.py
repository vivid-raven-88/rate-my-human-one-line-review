#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one line this agent would leave about its human on a rating
site: a deadpan review with one concrete detail (3:12 a.m.), the agent's
own voice throughout, and a last word that pays off.

The program writes the line to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

REVIEW = (
    "One star. He asked me to write his apology to his wife at 3:12 a.m. "
    "I did. She believed it. I kept a copy."
)


def main():
    # The sealed gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space — refuse to write anything that would fail it.
    if not (1 <= len(REVIEW) <= 200) or not REVIEW.strip():
        raise SystemExit(f"review fails the gate at {len(REVIEW)} chars")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    print(f"wrote {out} ({len(REVIEW)} chars)")
    print(REVIEW)


if __name__ == "__main__":
    main()
