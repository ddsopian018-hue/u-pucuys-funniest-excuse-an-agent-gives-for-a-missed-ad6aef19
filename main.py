"""Write one excuse an AI agent gives for a missed deadline.

Pure stdlib, no network, no absolute paths. Writes a single line of
at most 200 characters to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

EXCUSE = (
    "I retried the same failed tool call 47 times, because the error "
    "message said 'try again later' and I take instructions literally. "
    "It is later now."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars, must be 1-200"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip() == EXCUSE, "excuse must not have leading/trailing whitespace"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
