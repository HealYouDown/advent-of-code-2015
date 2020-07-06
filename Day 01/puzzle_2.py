with open("Day 01/input.txt", "r") as fp:
    data = fp.read()

floor = 0
for index, char in enumerate(data):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    if floor == -1:
        print(index+1)
        break
