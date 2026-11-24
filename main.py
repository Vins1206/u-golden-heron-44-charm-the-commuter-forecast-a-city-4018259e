"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a
city that does not exist -- Drizzlewick -- to /output/entry.txt.

The line is a fixed, hand-written forecast: no randomness, no network,
no input files, so every run produces byte-identical output. It keeps
the rhythm of a broadcast forecast (greeting, place, weather, timing)
and bends it once, at the end, with a small joke for the bored
commuter waiting on the platform.
"""

import os

# One line, 138 characters: a forecast for Drizzlewick, a city that
# does not exist, with its weather and one smile for the commuter.
LINE = (
    "Good morning, Drizzlewick: light rain till nine, then sunshine "
    "on the platform \u2014 the 8:15 runs late, but the puddles are "
    "doing their best."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the one forecast
    # line, so the gate counts precisely the characters of the line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
