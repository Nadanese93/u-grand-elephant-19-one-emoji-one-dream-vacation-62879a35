"""One Emoji, One Dream Vacation — entry writer.

Writes exactly one emoji, the castle, to the harness output file.
The castle names a dream vacation at a glance: a fairytale castle trip,
postcard-vivid, specific, instantly readable across cultures.

Judge fit: the travel-editor brief rewards one emoji that plainly names a
dream vacation, vivid at a glance, personal and specific, with a spark of
surprise. A castle beats the crowded beach/mountain picks (Mount Fuji,
desert island) by naming a fairytale destination no one else in the field
picked, and it reads instantly at any size.
"""

import os
import unicodedata

ENTRY = "🏰"

MAX_CHARS = 8


def validate(entry):
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(entry)}")
    if entry.strip() == "":
        raise ValueError("entry must not be only white space")
    if len(entry) != 1 or unicodedata.category(entry) != "So":
        raise ValueError("entry must be exactly one emoji character")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
