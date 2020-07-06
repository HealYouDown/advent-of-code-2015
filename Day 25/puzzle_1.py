from typing import Tuple
import numpy as np
import sys

class Grid:
    def __init__(self, size: Tuple[int, int]):
        self.width, self.height = size

    def get_value_for_position(self, position: Tuple[int, int]) -> int:
        x, y = position

        rows = []
        row_stepper = 1
    
        for y_position in range(self.height):
            row = []
            # Set the first number of the row
            if y_position == 0:
                row.append(1)
            else:
                row.append(rows[y_position-1][0] + row_stepper)
                row_stepper += 1
    
            # set initial col stepper based on row
            col_stepper = y_position + 2

            for x_position in range(1, self.width): 
                row.append(row[x_position-1] + col_stepper)
                col_stepper += 1

            rows.append(row)

            if y_position == y:
                return rows[y_position][x]

    def get_code_for_value(self, value: int) -> int:
        codes = [20151125]

        while len(codes) < value:
            codes.append((codes[-1] * 252533) % 33554393)

        return codes[-1]

if __name__ == "__main__":
    puzzle_input = 2981, 3075
    grid_size = 10000, 10000

    grid = Grid(grid_size)
    value = grid.get_value_for_position((puzzle_input[1]-1, puzzle_input[0]-1))
    code = grid.get_code_for_value(value)
    print(value, code)
