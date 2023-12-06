[
    (importlib := __import__("importlib")),
    (sys := importlib.import_module("sys")),
    (os := __import__("os", globals(), locals(), ["path"], 0)),
    (path := os.path),
    (rich := __import__("rich", globals(), locals(), ["print"], 0)),
    (print := rich.print),
    (solve := (lambda data: print("Answer:", None))),
    [
        (use_test := (len(sys.argv) == 2 and sys.argv[-1] == "--test")),
        (
            input_path := path.join(
                path.dirname(__file__), "input.txt" if not use_test else "test.txt"
            )
        ),
        (data := open(input_path).read().split("\n")),
        solve(data),
    ]
    if __name__ == "__main__"
    else ...,
]
