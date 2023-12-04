import * as fs from "fs";
import { join } from "path";

export const INPUT_FILE = join(__dirname, "input.txt");
const data = fs.readFileSync(INPUT_FILE, "utf-8").split("\n");

const symbol = (char: string) => /[^\d|\.]/g.test(char);
const digit = (char: string) => /\d/.test(char);
const getAdjacentPositions = (row: number, end: number): [number, number][] => {
    const prevRow = row - 1;
    const nextRow = row + 1;

    return [
        [prevRow, end - 1],
        [prevRow, end],
        [prevRow, end + 1],
        [row, end - 1],
        [row, end + 1],
        [nextRow, end - 1],
        [nextRow, end],
        [nextRow, end + 1],
    ];
};

let total = 0;
for (const [row, line] of data.entries()) {
    for (let col = 0; col < line.length; col++) {
        const char = line[col];

        if (symbol(char)) {
            continue;
        }

        let number = "";
        let end = col;
        let isAdj = false;

        while (digit(line[end]) && end < line.length) {
            number += line[end];

            for (const [r, c] of getAdjacentPositions(row, end)) {
                isAdj ||=
                    r > 0 &&
                    r < data.length &&
                    c > 0 &&
                    c < data[r].length &&
                    symbol(data[r][c]);
            }

            end++;
        }

        if (!number) {
            continue;
        }

        if (isAdj) {
            total += parseInt(number);
        }

        col += number.length;
    }
}

console.log("Answer:", total);
