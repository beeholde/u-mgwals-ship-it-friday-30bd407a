import os
import sys

LINE = "fix: shipped the Friday rewrite to prod, tests still running \u2014 you're welcome."


def resolve_output_dir():
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return "/output"


# Gate: 1-159 chars, single line, no trailing newline in output.
def validate(text):
    if not isinstance(text, str):
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    count = len(text)
    if count < 1 or count > 159:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(LINE):
        sys.stderr.write("entry line failed validation\n")
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(out_path, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
