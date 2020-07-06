with open("Day 01/input.txt", "r") as fp:
    data = fp.read()

floor = 0
floor += data.count("(")
floor -= data.count(")")
print(floor)
