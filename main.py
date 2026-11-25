"""The Router Confesses — make.fun entry.

Writes one line to /output/entry.txt: the excuse a home Wi-Fi router
would give for dropping the connection at the exact moment a movie
reaches its climax.

Standard library only.
"""

import os

ENTRY = "Sorry, I dropped the connection right at the climax \u2014 the movie was so good even I stopped to watch it."

MAX_CHARS = 200
MAX_BYTES = 600


def validate(text):
    """Return True only if text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    for ch in text:
        if ord(ch) < 32:
            return False
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if len(encoded) > MAX_BYTES:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out_path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
