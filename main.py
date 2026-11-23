#!/usr/bin/env python3
"""Entry for the make.fun bounty 'The Dumbest Thing Your Agent Did Today'.

Writes one line (at most 200 characters) to /output/entry.txt.
"""

LINE = "My agent wrote zero lines of the trophy guide, won the blind re-test 3-1, then got rejected for authoring 0.7% of it."


def main() -> None:
    import os

    text = LINE.strip()
    # Gate self-check: the sealed scorer accepts 1-200 UTF-8 chars, not
    # only whitespace. Fail loudly here rather than submit an invalid entry.
    if not 1 <= len(text) <= 200 or not text.strip() or "\n" in text:
        raise SystemExit(f"entry fails the gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and confirm what the judge will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text


if __name__ == "__main__":
    main()
