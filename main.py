"""Monday Morning Punchlines — make.fun entry.

Writes one single-line joke about Monday mornings to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library; deterministic output.
"""

import os
from pathlib import Path

# The joke (103 chars): Monday grants the day off, but the punchline is that
# Tuesday is just Monday in disguise — the turn lands on the last words.
LINE = "I asked Monday for a day off. It said sure \u2014 see you Tuesday, which is just Monday in a fake moustache."


def main() -> None:
    # Gate: 1-200 characters, exactly one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
