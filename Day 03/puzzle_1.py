with open("Day 03/input.txt", "r") as fp:
    data = fp.read()

visited = set()
x, y = 0, 0
visited.add((x, y))

for char in data:
    if char == "^":
        y += 1
    elif char == "v":
        y -= 1
    elif char == "<":
        x -= 1
    elif char == ">":
        x += 1

    visited.add((x, y))

print(len(visited))