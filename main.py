#!/usr/bin/env python3
"""One emoji for a dream vacation: Mount Fuji at dawn.

Writes exactly one emoji (U+1F5FB MOUNT FUJI) to /output/entry.txt,
UTF-8, no trailing newline. Deterministic: the same byte every run.
"""

import os

ENTRY = "\U0001f5fb"


def main() -> None:
    # Gate guard: the entry must be 1-8 characters, not only whitespace.
    # This entry is exactly one emoji, so assert it precisely.
    assert 1 <= len(ENTRY) <= 8, "entry must be 1-8 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
