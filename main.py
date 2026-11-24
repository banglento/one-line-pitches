#!/usr/bin/env python3
"""Entry generator for the make.fun bounty "A Day of One-Line Pitches".

Writes the one-sentence pitch to /output/entry.txt (creating /output
if needed). Standard library only.
"""

import os

ENTRY = (
    "Tell make.fun your app idea in plain words and an AI agent builds "
    "it for you \u2014 no code, no setup, no waiting: just describe it "
    "and watch your first app come to life."
)

# Competition gate: /output/entry.txt must be 1 to 240 characters.
MAX_CHARS = 240


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
