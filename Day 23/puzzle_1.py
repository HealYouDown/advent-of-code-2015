from typing import List


class Instruction:
    def __init__(self, line: str):
        self.instruction = line[0:3]
        if self.instruction in ["hlf", "tpl", "inc", "jmp"]:
            self.arg1 = line[4:]
            self.arg2 = None
        elif self.instruction in ["jie", "jio"]:
            self.arg1, self.arg2 = line[4:].strip().split(", ")

    def __repr__(self) -> str:
        return f"<Instruction {self.instruction} arg1={self.arg1} arg2={self.arg2}>"

    def execute(self, stack: dict, index: int) -> int:
        if self.instruction == "hlf":
            stack[self.arg1] //= 2
            index += 1

        elif self.instruction == "tpl":
            stack[self.arg1] *= 3
            index += 1

        elif self.instruction == "inc":
            stack[self.arg1] += 1
            index += 1

        elif self.instruction == "jmp":
            index += int(self.arg1)

        elif self.instruction == "jie":
            if stack[self.arg1] % 2 == 0:
                index += int(self.arg2)
            else:
                index += 1

        elif self.instruction == "jio":
            if stack[self.arg1] == 1:
                index += int(self.arg2)
            else:
                index += 1

        else:
            raise NotImplementedError

        return index


class Computer:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.index = 0
        self.stack = {
            "a": 0,
            "b": 0
        }

    def run(self):
        while True:
            try:
                inst = self.instructions[self.index]
                self.index = inst.execute(self.stack, self.index)
            except (NotImplementedError, IndexError) as e:
                print(e)
                print(self.stack)
                break


if __name__ == "__main__":
    with open("Day 23/input.txt", "r") as fp:
        instructions = [Instruction(l.strip()) for l in fp.readlines()]

    computer = Computer(instructions)
    computer.run()
