import re
import enum

class Action(enum.Enum):
    toggle = 0
    turn_on = 1
    turn_off = 2


with open("Day 06/input.txt", "r") as fp:
    data = [l.strip() for l in fp.readlines()]
    instructions = []
    for line in data:
        match = re.match(r"(turn on|turn off|toggle) (\d*,\d*) through (\d*,\d*)", line.strip())
        
        action = None
        if match.group(1) == "toggle":
            action = Action.toggle
        elif match.group(1) == "turn on":
            action = Action.turn_on
        else:
            action = Action.turn_off

        start_x, start_y = [int(i) for i in match.group(2).split(",")]
        end_x, end_y = [int(i) for i in match.group(3).split(",")]

        instructions.append((action, start_x, start_y, end_x, end_y))

# Create grid
grid = [[0 for _ in range(1000)] for _ in range(1000)]

# Execute instructions
for instruction in instructions:
    action, x, y, w, h = instruction

    for row_index in range(y, h+1):
        for col_index in range(x, w+1):

            if action == Action.turn_off:
                grid[row_index][col_index] -= 1
                if grid[row_index][col_index] < 0:
                    grid[row_index][col_index] = 0
                
            elif action == Action.turn_on:
                grid[row_index][col_index] += 1

            elif action == Action.toggle:
                grid[row_index][col_index] += 2

all_lights = []
for row in grid:
    all_lights.extend(row)

print(sum(all_lights))
