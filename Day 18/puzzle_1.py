import numpy as np
import copy

"""
adding a border around the grid with all lights
off to be able to index properly.
border is ignored when going through the rows
"""

with open("Day 18/input.txt", "r") as fp:
    rows = []
    for line in fp.readlines():
        chars = [c for c in line.strip()]
        chars.insert(0, ".")
        chars.append(".")
        rows.append(chars)

    col_length = len(rows[0])
    rows.insert(0, ["." for _ in range(col_length)])
    rows.insert(len(rows)+1, ["." for _ in range(col_length)])


def animate(grid) -> None:
    grid_copy = copy.deepcopy(grid)

    row_length = len(grid_copy)
    col_length = len(grid_copy[0])

    for row_index in range(row_length):
        for col_index in range(col_length):
            if (row_index >= 1 and col_index >= 1
                    and row_index+2 <= row_length and col_index+2 <= col_length):
                lights_around = copy.deepcopy(grid_copy[row_index-1:row_index+2, col_index-1:col_index+2])
                # remove center
                center = lights_around[1,1]
                lights_around[1,1] = "o"

                lights = []
                for row in lights_around:
                    lights.extend(row)
                lights.remove("o")

                on_count = lights.count("#")

                if center == "#" and on_count not in [2, 3]:
                    grid[row_index, col_index] = "."
                elif center == "." and on_count == 3:
                    grid[row_index, col_index] = "#"

if __name__ == "__main__":
    grid = np.array(rows, np.str)
    for _ in range(100):
        animate(grid)
        
    # count lights that are on
    total = 0
    for row in grid:
        total += list(row).count("#")

    print(total)
