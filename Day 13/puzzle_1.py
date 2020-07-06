import re
from collections import defaultdict
from itertools import permutations

with open("Day 13/input.txt", "r") as fp:
    guest_data = defaultdict(dict)

    for line in fp.readlines():
        match = re.match(r"(.*) would (gain|lose) (\d*) happiness units by sitting next to (.*).",
                         line)

        guest = match.group(1)
        factor = 1 if match.group(2) == "gain" else -1
        amount = int(match.group(3))
        neighbor = match.group(4)

        guest_data[guest][neighbor] = amount * factor


highest_happiness = 0
perms = list(permutations(guest_data.keys()))

for perm in perms:
    happiness = 0
    for index, guest in enumerate(perm):
        if index == 0:
            neighbor_1 = perm[-1]
            neighbor_2 = perm[index+1]
        elif index == len(perm)-1:
            neighbor_1 = perm[0]
            neighbor_2 = perm[index-1]
        else:
            neighbor_1 = perm[index-1]
            neighbor_2 = perm[index+1]

        happiness += guest_data[guest][neighbor_1] + guest_data[guest][neighbor_2]

    if happiness > highest_happiness:
        highest_happiness = happiness

print(highest_happiness)
