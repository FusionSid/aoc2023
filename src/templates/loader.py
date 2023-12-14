""" (module) loader
Loads input files and runs the `solve` function
"""

__all__ = ("load_input",)

from sys import argv
from typing import Callable
from time import perf_counter
from os.path import join, dirname

from rich import print

solve_function_t = Callable[[list[str]], None]


def time_call(
    solve_function: solve_function_t,
    data: list[str],
    time_calls: bool,
    name: str | None,
) -> None:
    if not time_calls:
        return solve_function(data)

    start = perf_counter()
    solve_function(data)
    stop = perf_counter()

    print(f"{name}: {stop - start}")


def load_input(file: str, solve: solve_function_t, spl="\n") -> None:
    use_test = "--test" in argv
    use_main = not use_test
    use_test |= "--both" in argv

    time_calls = "--time" in argv

    test_input_path = join(dirname(file), "test.txt")
    main_input_path = join(dirname(file), "input.txt")

    if use_test:
        with open(test_input_path) as f:
            data = f.read().split(spl)
            time_call(solve, data, time_calls, "TEST")

    if use_main:
        with open(main_input_path) as f:
            data = f.read().split(spl)
            time_call(solve, data, time_calls, "MAIN")
