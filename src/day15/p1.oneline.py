((print := __import__("rich", globals(), locals(), ["print"], 0).print), (load_input := __import__("loader", globals(), locals(), ["load_input"], 0).load_input), (solve := (lambda data: print(sum([(cv := 0), [[(cv := cv + ord(c)), (cv := cv * 17), (cv := cv % 256)] for c in i], cv][-1] for i in data)))), load_input(__file__, solve, ",") if __name__ == "__main__" else ...)
