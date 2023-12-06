import shutil
import webbrowser
from pathlib import Path
from os import path, environ, mkdir

import typer
import dotenv
import requests
from rich import print


SRC_DIR = path.dirname(__file__)
TEMPLATE_DIR = path.join(SRC_DIR, "templates/")


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

    Path(path.join(DIRECTORY, "test.txt")).touch()  # test input file

    loader_path = path.join(TEMPLATE_DIR, "loader.py")
    shutil.copyfile(loader_path, path.join(DIRECTORY, "loader.py"))

    oneliner_path = path.join(TEMPLATE_DIR, "oneliner.py")
    for oneliner in ["p1.oneline.py", "p2.oneline.py"]:
        shutil.copyfile(oneliner_path, path.join(DIRECTORY, oneliner))

    original_path = path.join(TEMPLATE_DIR, "original.py")
    for original in ["p1.orig.py", "p2.orig.py"]:
        shutil.copyfile(original_path, path.join(DIRECTORY, original))

    print("[b green]All Files Created!")

    print("[b green]Setup Complete! Opening Challenge In Browser...")
    webbrowser.open(f"https://adventofcode.com/2023/day/{day}")


if __name__ == "__main__":
    dotenv.load_dotenv()
    typer.run(main)
