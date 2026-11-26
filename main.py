"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
framed as an ancient artifact, to /output/entry.txt.

The placard: a stapler recast as the binder of oaths. Its function
(stapling things together) becomes the conceit: in a lost Department
of Perpetual Meetings, oaths were not sworn, they were stapled.
The donor line sells the deadpan curator voice.
"""

import os

PLACARD = (
    "Stapler, c. 1987, pressed steel. "
    "Bound the oaths of the Department of Perpetual Meetings; "
    "each staple a promise nobody kept. "
    "Donated by Mr. Henderson."
)


def main() -> None:
    text = PLACARD.strip()
    assert text, "placard must not be empty"
    assert "\n" not in text, "placard must be exactly one line"
    assert 1 <= len(text) <= 180, f"placard is {len(text)} chars, must be 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        # One line, 150 characters, trailing newline only.
        f.write(text + "\n")


if __name__ == "__main__":
    main()
