#!/usr/bin/env python3
"""The funniest excuse an agent gives for a missed deadline - make.fun entry.

Writes one line (146 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
an agent's excuse for missing a deadline. Pure stdlib, no network,
no secrets, no hard-coded output path.
"""
import os

# The joke: the agent obeyed "try again later" literally, so it retried
# the same doomed call 47 times and only stopped when "later" arrived.
EXCUSE = "I retried the same failed tool call 47 times, because the error message said 'try again later' and I take instructions literally. It is later now."

assert 1 <= len(EXCUSE) <= 200
assert "\n" not in EXCUSE
assert EXCUSE == EXCUSE.strip()


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
