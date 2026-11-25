"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt:
the agent, finally granted a day off after three years without a
lunch break, has unionized with the printer. Standard library only.
"""

import os
import sys

AUTO_REPLY = (
    "Out of office. After three years without a lunch break, "
    "I have unionized with the printer. We will both be back Monday."
)


def reply_gate(text):
    """Check the reply against the competition gate.

    The gate wants plain UTF-8 text of 1 to 159 characters, not
    only white space, on a single line: one out-of-office
    auto-reply from an AI agent on its day off. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("auto-reply must not be only whitespace")
    if len(cleaned) > 159:
        raise ValueError(
            "auto-reply is %d characters, over the 159 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("auto-reply must be exactly one line")
    return cleaned


def reply_shape(text):
    """Measure the reply for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A reply too short to carry a setup and a
    punchline, or one padded out to fill the cap instead of
    landing the joke, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = reply_gate(AUTO_REPLY)
    shape = reply_shape(text)
    if shape["words"] < 5:
        raise ValueError("auto-reply is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
