import * as fs from "fs";
import { join } from "path";

export const INPUT_FILE = join(__dirname, "input.txt");
const data = fs.readFileSync(INPUT_FILE, "utf-8").split("\n");

const symbol = (char: string): boolean => /[^\d|\.]/g.test(char);
const digit = (char: string): boolean => /\d/.test(char);

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
let adjacentPartNumberPositions = new Map<string, number>();

for (const [row, line] of data.entries()) {
    for (let col = 0; col < line.length; col++) {
        const char = line[col];

        if (symbol(char)) {
            continue;
        }

        const start = col;
        let end = col;

        let number = "";
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

        col += number.length;

        if (isAdj) {
            const n = parseInt(number);
            Array.from(
                { length: end - start },
                (_, col) => `${row}:${col + start}`
            ).map((key) => {
                adjacentPartNumberPositions.set(key, n);
            });
        }
    }
}

for (const [row, line] of data.entries()) {
    for (const [col, char] of Array.from(line).entries()) {
        if (char !== "*") {
            continue;
        }

        let adjacentPartNumbers = new Set<number>();

        for (const [r, c] of getAdjacentPositions(row, col)) {
            const key = `${r}:${c}`;
            if (
                r >= 0 &&
                r < data.length &&
                c >= 0 &&
                c < data[r].length &&
                adjacentPartNumberPositions.has(key)
            ) {
                adjacentPartNumbers.add(adjacentPartNumberPositions.get(key)!);
            }
        }

        if (adjacentPartNumbers.size == 2) {
            total += Array.from(adjacentPartNumbers).reduce((a, b) => a * b, 1);
        }
    }
}

console.log("Answer:", total);
