from rich import print
from PIL import Image, ImageDraw

from loader import load_input

NEIGHBOURS: dict[str, tuple[int, ...]] = {
    #     L  R  U  D
    "7": (1, 0, 0, 1),
    "L": (0, 1, 1, 0),
    "J": (1, 0, 1, 0),
    "F": (0, 1, 0, 1),
    "-": (1, 1, 0, 0),
    "|": (0, 0, 1, 1),
    ".": (0, 0, 0, 0),
    "S": (1, 1, 1, 1),
}

IMAGE_LINES = {
    "7": [
        (0, 5, 10, 5),
        (10, 5, 10, 15),
        (0, 10, 5, 10),
        (5, 10, 5, 15),
    ],
    "L": [
        (5, 10, 5, 0),
        (15, 10, 5, 10),
        (10, 5, 10, 0),
        (15, 5, 10, 5),
    ],
    "J": [
        (0, 5, 5, 5),
        (5, 5, 5, 0),
        (0, 10, 10, 10),
        (10, 10, 10, 0),
    ],
    "F": [
        (5, 5, 5, 15),
        (5, 5, 15, 5),
        (10, 10, 10, 15),
        (10, 10, 15, 10),
    ],
    ".": [],
    "S": [(5, 5, 10, 5), (10, 5, 10, 10), (10, 10, 5, 10), (5, 10, 5, 5)],
    "-": [(0, 5, 15, 5), (0, 10, 15, 10)],
    "|": [(5, 0, 5, 15), (10, 0, 10, 15)],
}


def get_tiles_drawn(color: str):
    tiles_drawn = {}
    for tile_t, lines in IMAGE_LINES.items():
        img = Image.new("RGB", (15, 15))
        draw = ImageDraw.Draw(img)
        for line in lines:
            draw.line(line, fill=color, width=1)
        tiles_drawn[tile_t] = img
    return tiles_drawn


def show_canvas(data: list[str]):
    tiles_drawn = get_tiles_drawn("white")
    canvas_size = 15 * len(data)
    canvas = Image.new("RGB", (canvas_size, canvas_size), "black")

    x, y = 0, 0
    for line in data:
        for tile in line:
            canvas.paste(tiles_drawn[tile], (x, y))
            x = (x + 15) % canvas_size
        y = (y + 15) % canvas_size

    return canvas


def find_start(data: list[str]) -> tuple[int, int]:
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == "S":
                return (x, y)

    return (-1, -1)


def get_neighbours(pos: tuple[int, int], node_type: str, data):
    x, y = pos
    all_neighbour_positions = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    neighbours = [
        pos
        for pos, use_pos in zip(all_neighbour_positions, NEIGHBOURS[node_type])
        if use_pos
    ]

    if node_type == "S":
        actual_neighbours = []
        for n in neighbours:
            nsn = get_neighbours(n, data[n[1]][n[0]], data)
            print(nsn)
            if pos in nsn:
                actual_neighbours.append(n)

        return actual_neighbours

    return [
        (px, py)
        for px, py in neighbours
        if px >= 0 and px < len(data) and py >= 0 and py < len(data)
    ]


def solve(data: list[str]) -> None:
    canvas = show_canvas(data)
    tiles_drawn = get_tiles_drawn("red")

    start_pos = find_start(data)

    visited = set()
    queue = [start_pos]

    image = canvas.copy()
    while queue:
        node = queue.pop(0)
        symbol = data[node[1]][node[0]]

        image.paste(
            tiles_drawn[symbol],
            (
                ((node[0] + 15) % len(data) * 15),
                ((node[1] + 15) % len(data) * 15),
            ),
        )

        for neighbour in get_neighbours(node, symbol, data):
            if neighbour not in visited:
                queue.append(neighbour)
            visited.add(node)

    canvas.show()
    image.show()

    print(len(visited) // 2)


if __name__ == "__main__":
    load_input(__file__, solve)
