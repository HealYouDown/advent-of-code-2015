import sys
INPUT = 36000000

class House:
    def __init__(self, nr: int):
        self.nr = nr
        self.presents = 0 

    def __repr__(self) -> str:
        return f"<House {self.nr}: {self.presents} Presents>"

    def deliver_presents(self, amount: int) -> None:
        self.presents += amount

        if self.presents >= INPUT:
            print(repr(self))
            sys.exit()


limit = 1000000
houses = [House(i) for i in range(1, limit+1)]

for elf in range(1, limit+1):
    for index in range(0, limit+1, elf):
        if index == 0 and elf != 0:
            continue
        houses[index-1].deliver_presents(elf*10)
