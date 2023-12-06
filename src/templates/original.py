import sys
from os import path

from rich import print


def solve(data: list[str]) -> None:
    print("Answer:", None)


if __name__ == "__main__":
    use_test = len(sys.argv) == 2 and sys.argv[-1] == "--test"
    input_path = path.join(
        path.dirname(__file__), "test.txt" if use_test else "input.txt"
    )

    with open(input_path) as f:
        data = f.read().split("\n")

    solve(data)
