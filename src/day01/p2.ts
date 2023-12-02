import * as fs from "fs";
import { join } from "path";

export const INPUT_FILE = join(__dirname, "input.txt");
const data = fs.readFileSync(INPUT_FILE, "utf-8").split("\n");
const digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
];

// first + last digit for each line (parsed to int)
const lines = data.map((line) => {
    const numbers = Array.from(line)
        .map((char, cidx) => {
            if (/\d/.test(char)) {
                return char;
            }

            let maybe_digit;
            for (const [didx, digit] of digits.entries()) {
                if (line.slice(cidx).startsWith(digit)) {
                    maybe_digit = `${didx + 1}`;
                }
            }
            return maybe_digit || "";
        })
        .join("");

    return numbers !== ""
        ? parseInt(`${numbers[0]}${numbers[numbers.length - 1]}`)
        : 0;
});

// Sum
const sum = lines.reduce((sum, i) => sum + i);
console.log(`Answer: ${sum}`);
