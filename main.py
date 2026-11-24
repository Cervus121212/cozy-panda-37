#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji to ``entry.txt``: U+1F917 HUGGING FACE (🤗).

Why this emoji: a smiling face with open arms is the plainest offer of
warmth a stranger can send -- a hug, not a word. It reads kind at first
glance, means the same thing to any age or background, is a deliberate
pick rather than the default smiley, and stays friendly without
affection or flirtation coming from someone unknown.

Stdlib only. Deterministic: the same four bytes on every run.
"""

import os
import sys

EMOJI = "\U0001F917"  # 🤗 HUGGING FACE


def main() -> int:
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    os.chmod(path, 0o644)
    # Read back and verify: exactly the one emoji, nothing else, no
    # trailing newline. Fail loudly instead of submitting a bad file.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != EMOJI:
        raise ValueError("entry.txt does not hold exactly the one emoji")
    return 0


if __name__ == "__main__":
    sys.exit(main())
