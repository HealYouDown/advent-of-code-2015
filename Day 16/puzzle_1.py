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
    if all(gift_aunt[key] == value for key, value in attributes.items()):
        print(aunt)
        break
