"""Two-Sentence Horror.

Writes one horror story of exactly two sentences (1-400 characters)
to /output/entry.txt (or the path named by ENTRY_OUT / ENTRY_OUT_DIR
when those are set).

The story: a doorbell camera catches a man testing every door of the
house at night. The narrator watches the clip twice, reassured that
the locks held -- until the timestamps show the man worked through
the doors in the exact order she locks them, and the last clip came
from the camera in her bedroom, twenty minutes ago.
"""

import os
import sys

ENTRY_TEXT = (
    "The doorbell camera caught a man testing every door of my house "
    "at 3 in the morning, and I watched the clip twice, telling myself "
    "the locks had held. Then I saw the timestamps: he tested them in "
    "the exact order I lock them every night, and the last clip came "
    "from the camera in my bedroom, twenty minutes ago."
)

MIN_CHARS = 1
MAX_CHARS = 400
EXPECTED_SENTENCES = 2


def check_length(text):
    """The gate counts characters: 1 to 400, no more, no fewer."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )


def count_sentence_stops(text):
    """How many sentence-ending marks the text holds."""
    return sum(1 for ch in text if ch in ".!?")


def check_two_sentences(text):
    """Exactly two sentences: two sentence-ending stops, text ends on one.

    The story uses no abbreviations, so every '.' is a sentence end.
    """
    stops = count_sentence_stops(text)
    if stops != EXPECTED_SENTENCES:
        raise ValueError(
            f"entry has {stops} sentence-ending marks, "
            f"must have {EXPECTED_SENTENCES}"
        )
    if text[-1] not in ".!?":
        raise ValueError("entry must end on a sentence-ending mark")


def check_plain_block(text):
    """One block of plain text: not blank, no line breaks, no control chars,
    and no stray leading or trailing space (the gate counts every char)."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single block with no line breaks")
    for ch in text:
        if ord(ch) < 0x20 and ch != "\t":
            raise ValueError(f"entry holds a control character {ch!r}")


def build_entry():
    """Validate the story against every part of the bounty gate."""
    check_length(ENTRY_TEXT)
    check_two_sentences(ENTRY_TEXT)
    check_plain_block(ENTRY_TEXT)
    return ENTRY_TEXT


def resolve_output_path():
    if os.environ.get("ENTRY_OUT"):
        return os.environ["ENTRY_OUT"]
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = build_entry()
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
