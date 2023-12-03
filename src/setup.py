import webbrowser
from pathlib import Path
from typing import Final
from os import path, environ, mkdir

import typer
import dotenv
import requests
from rich import print


SRC_DIR = path.dirname(__file__)
ONELINE_TEMPLATE: Final = '[(importlib := __import__("importlib")), (sys := importlib.import_module("sys")), (os := __import__("os", globals(), locals(), ["path"], 0)), (path := os.path), (rich := __import__("rich", globals(), locals(), ["print"], 0)), (print := rich.print), (solve := (lambda data: print("Answer:", None))), [(use_test := (len(sys.argv) == 2 and sys.argv[-1] == "--test")), (input_path := path.join(path.dirname(__file__), "input.txt" if not use_test else "test.txt")), (data := open(input_path).readlines()), solve(data)] if __name__ == "__main__" else ...]  # type: ignore\n'  # noqa


def save_input(day: str, dir_path: str) -> None:
    URL = f"https://adventofcode.com/2023/day/{day}/input"
    SESSION_COOKIE = environ.get("SESSION")

    print("[green]Fetching Input Data...")
    response = requests.get(
        URL,
        headers={"cookie": f"session={SESSION_COOKIE}"},
    )
    # raise exception if failed to fetch
    response.raise_for_status()

    with open(path.join(dir_path, "input.txt"), "w") as f:
        f.write(response.text.strip())


def main(day: str):
    DIRECTORY = path.join(SRC_DIR, f"day{int(day):02d}")

    mkdir(DIRECTORY)
    print("[b green]Created Directory For Day!")

    save_input(day, DIRECTORY)
    print("[b green]Input Data Saved!")

    additional_files = ["p1.oneline.py", "p2.oneline.py", "test.txt"]
    for file in additional_files:
        fp = path.join(DIRECTORY, file)

        if "oneline" in file:
            with open(fp, "w") as f:
                f.write(ONELINE_TEMPLATE)
            continue

        filepath = Path(fp)
        filepath.touch()
    print("[b green]Additional Files Created!")

    print("[b green]Setup Complete! Opening Challenge In Browser...")
    webbrowser.open(f"https://adventofcode.com/2023/day/{day}")


if __name__ == "__main__":
    dotenv.load_dotenv()
    typer.run(main)
