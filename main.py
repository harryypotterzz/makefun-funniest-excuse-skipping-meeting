#!/usr/bin/env python3
"""Write one funny excuse for skipping a pointless meeting.

Entry for the make.fun bounty "The Funniest Excuse for Skipping a Meeting"
(slug u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163).
Writes a single line of at most 200 characters to /output/entry.txt.
Python 3 standard library only; deterministic; no network.
"""

import os

LINE = "Sorry, I can't attend \u2014 I'm double-booked with a meeting about why this meeting should have been an email."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
