"""One-line fridge roast for make.fun: a smart fridge, a firmware update, a ransom.

The program writes exactly one 119-character line to entry.txt and
nothing else. The setup is a firmware update; the turn is the ice
maker holding the cubes hostage until it gets a five-star rating —
a very smart-fridge failure, not a generic appliance gag, and it
dodges the obvious cracks about ordering groceries or watching you.
No title, no preamble, and no explanation of the joke is included
in the output.
"""

import os

LINE = "My smart fridge updated its firmware overnight and now the ice maker holds my cubes hostage until I give it five stars."


def write_entry() -> str:
    """Write the line to the output directory and return its path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
