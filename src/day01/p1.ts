import * as fs from "fs";
import { join } from "path";

export const INPUT_FILE = join(__dirname, "input.txt");
const data = fs.readFileSync(INPUT_FILE, "utf-8").split("\n");

// first + last digit for each line (parsed to int)
const numbers = data.map((line) => {
    const digits = Array.from(line.trimEnd())
        .filter((char) => /\d/.test(char))
        .join("");
    return parseInt(`${digits[0]}${digits[digits.length - 1]}`);
});

// Sum
const sum = numbers.reduce((sum, i) => sum + i);
console.log(`Answer: ${sum}`);
