from rich import print
from loader import load_input


def solve(data: list[str]) -> None:
    print("Answer:", data)


if __name__ == "__main__":
    load_input(__file__, solve)
