import itertools

class Container:
    def __init__(self, line):
        self.size = int(line)

    def __repr__(self) -> str:
        return f"<Container size={self.size}>"

    def __radd__(self, other):
        return other + self.size

with open("Day 17/input.txt", "r") as fp:
    containers = [Container(l) for l in fp.readlines()]

combinations = []
for i in range(1, len(containers)+1):
    for comb in itertools.combinations(containers, i):
        if sum(comb) == 150:
            combinations.append(comb)

print(len(combinations))
shortest = len(sorted(combinations, key=len, reverse=False)[0])
print(len(list(filter(lambda l: len(l) == shortest, combinations))))

