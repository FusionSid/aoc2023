[(importlib := __import__("importlib")),(sys := importlib.import_module("sys")),(os := __import__("os", globals(), locals(), ["path"], 0)),(path := os.path),(rich := __import__("rich", globals(), locals(), ["print"], 0)),(print := rich.print),(digits := ["one","two","three","four","five","six","seven","eight","nine",]),(solve := (lambda data: print(sum(map(lambda digits: int(digits[0] + digits[-1]) if digits else 0, map(lambda line: "".join(char if char.isdigit() else [(maybe := list(filter(lambda x: x is not Ellipsis, [ str(didx + 1) if line[idx:].startswith(digit) else ... for didx, digit in enumerate(digits) ],))),maybe[0] if maybe else "", ][-1] for idx, char in enumerate(line)),data,),),)))),[(use_test := (len(sys.argv) == 2 and sys.argv[-1] == "--test")),(input_path := path.join(path.dirname(__file__), "input.txt" if not use_test else "test.txt")), (data := open(input_path).readlines()), solve(data), ] if __name__ == "__main__" else ...,]  # type: ignore