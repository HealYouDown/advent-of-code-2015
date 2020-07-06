import re
from collections import defaultdict

with open("Day 16/input.txt", "r") as fp:
    aunts = defaultdict(dict)

    for line in fp.readlines():
        match = re.match(r"(.*): (.*): (\d*), (.*): (\d*), (.*): (\d*)",
                         line)

        name = match.group(1)
        for i in range(2, 7, 2):
            attr = match.group(i)
            attr_value = int(match.group(i+1))
            aunts[name][attr] = attr_value

gift_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for aunt, attributes in aunts.items():
    for key, value in attributes.items():

        if key in ["cats", "trees"]:
            if not gift_aunt[key] < value:
                break

        if key in ["pomeranians", "goldfish"]:
            if not gift_aunt[key] > value:
                break

        if key not in ["cats", "trees", "pomeranians", "goldfish"]:
            if gift_aunt[key] != value:
                break

    else:
        print(aunt, aunts[aunt])
        break
