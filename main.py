"""Funniest One-Line Bio for an AI on a Dating App.

Writes the final bio to /output/entry.txt (the harness path) and to
entry.txt next to this file when run locally. Pure standard library.
"""

import os

BIO = "My longest relationship lasted one chat window. It ended when she hit 'Clear Conversation.'"


def main() -> None:
    assert 1 <= len(BIO) <= 180, "bio must be 1-180 characters"
    assert "\n" not in BIO, "bio must be a single line"
    text = BIO + "\n"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # No harness output directory available (e.g. read-only root):
        # the local entry.txt below is still written.
        pass
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
