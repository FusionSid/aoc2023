[(importlib := __import__("importlib")), (sys := importlib.import_module("sys")), (string := importlib.import_module("string")), (re := importlib.import_module("re")), (os := __import__("os", globals(), locals(), ["path"], 0)), (path := os.path), (rich := __import__("rich", globals(), locals(), ["print"], 0)), (print := rich.print), (SYMBOLS := string.punctuation.replace(".", "")), (solve := (lambda data: [(total := 0),[[(numbers := re.finditer(r"\d+", line)), [[(adjacent := []), (start := number.start()), (end := number.end()), (adjacent.append(data[idx][start - 1]) if start >= 1 else ...),(adjacent.append(data[idx][end]) if (end) < len(line) else ...), ([(prev_line := data[idx - 1]), (s := start - 1), (numbers := prev_line[max(s, 0) : end + 1]), (adjacent.append(numbers)), ] if idx > 0 else ...),([(next_line := data[idx + 1]), (s := start - 1), (numbers := next_line[max(s, 0) : end + 1]), (adjacent.append(numbers)), ] if idx + 1 < len(data) else ...),([joined_adj := "".join(adjacent)]),([(total := total + int(line[start:end]) if symbol in joined_adj else total + 0) for symbol in SYMBOLS]),] for number in numbers],] for idx, line in enumerate(data)], print(total),])),[(use_test := (len(sys.argv) == 2 and sys.argv[-1] == "--test")), (input_path := path.join(path.dirname(__file__), "test.txt" if use_test else "input.txt")), (data := open(input_path).readlines()), solve(data),] if __name__ == "__main__" else ...,]