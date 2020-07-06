with open("Day 02/input.txt", "r") as fp:
    data = fp.readlines()

total = 0
for row in data:
    l, w, h = [int(dimension) for dimension in row.strip().split("x")]

    min1, min2 = sorted([l, w, h])[:2]
    wrap = 2*min1 + 2*min2

    volume = l*w*h

    ribbon = wrap + volume
    total += ribbon

print(int(total))
