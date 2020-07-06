with open("Day 03/input.txt", "r") as fp:
    data = fp.read()

class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def position(self) -> tuple:
        return self.x, self.y

    def move(self, char: str):
        if char == "^":
            self.y += 1
        elif char == "v":
            self.y -= 1
        elif char == "<":
            self.x -= 1
        elif char == ">":
            self.x += 1

visited = set()
santa = Santa()
robo_santa = Santa()

visited.add(santa.position)

for index, char in enumerate(data):
    if index % 2 == 0:
        santa.move(char)
        visited.add(santa.position)
    else:
        robo_santa.move(char)
        visited.add(robo_santa.position)

print(len(visited))
