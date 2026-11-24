#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

The program writes a single warm, surprising line (at most 200
characters) to /output/entry.txt, where the house gate scorer and
the judge read it.
"""

import os

LINE = (
    # One concrete detail (three blocks on the umbrella), one small
    # surprise (the dragonfly booking a seat), one warm turn (the rain
    # stopping exactly as I stepped out) — 157 characters, under the
    # 200-character gate.
    "This morning the rain stopped the second I stepped outside, "
    "and a dragonfly landed on my umbrella and rode three blocks "
    "with me, like it had booked the seat."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
