#!/usr/bin/env python3
"""Ship It Friday entry: write one commit-message line to /output/entry.txt.

The line is the funniest one-line git commit message an AI coding agent
writes right before breaking production on a Friday. Gate: UTF-8 text of
1 to 159 characters, not only whitespace, a single line, no trailing
newline.
"""
import os
import sys

LINE = "fix: deleted the error message \u2014 no errors, no problem. Happy Friday!"

def main() -> int:
    text = LINE
    chars = list(text)
    if not 1 <= len(chars) <= 159:
        print(f"entry must be 1-159 characters, got {len(chars)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    if data.decode("utf-8") != text:
        print("entry must be valid UTF-8", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
