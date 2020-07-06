import re

class Reindeer:
    def __init__(self, line: str):
        match = re.match(r"(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.",
                         line)
        self.name = match.group(1)
        self.speed = int(match.group(2))
        self.fly_time = int(match.group(3))
        self.rest_time = int(match.group(4))

        self.fly_counter = 0
        self.rest_counter = 0

        self.traveled = 0
        
        self.flying = True
        self.resting = False

    def __repr__(self) -> str:
        return f"<Reindeer {self.name} traveled={self.traveled}km>"

    def __lt__(self, other: "Reindeer"):
        return self.traveled > other.traveled

    def action(self):
        if self.flying:
            self.traveled += self.speed
            self.fly_counter += 1

        elif self.resting:
            self.rest_counter += 1

        if self.fly_counter == self.fly_time:
            self.fly_counter = 0
            self.resting = True
            self.flying = False

        elif self.rest_counter == self.rest_time:
            self.rest_counter = 0
            self.resting = False
            self.flying = True

if __name__ == "__main__":
    with open("Day 14/input.txt", "r") as fp:
        deers = [Reindeer(line) for line in fp.readlines()]

    seconds = 2503
    for _ in range(seconds):
        for deer in deers:
            deer.action()

    
    deers.sort()
    print(deers)
