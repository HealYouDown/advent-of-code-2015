import re
import enum
from typing import Union


class Action(enum.Enum):
    store = 0  # 123 -> x
    and_ = 1  # x AND y -> d
    or_ = 2  # x OR y -> e
    lshift = 3  # x LSHIFT 2 -> f
    rshift = 4  # y RSHIFT 2 -> g
    not_ = 5  # NOT e-> f


class Instruction:
    def __init__(self, line: str):
        # Parse instruction
        store_regex = r"(.*) -> (.*)", Action.store
        and_regex = r"(.*) AND (.*) -> (.*)", Action.and_
        or_regex = r"(.*) OR (.*) -> (.*)", Action.or_
        lshift_regex = r"(.*) LSHIFT (.*) -> (.*)", Action.lshift
        rshift_regex = r"(.*) RSHIFT (.*) -> (.*)", Action.rshift
        not_regex = r"NOT (.*) -> (.*)", Action.not_

        regex_patterns = [store_regex, and_regex, or_regex,
                          lshift_regex, rshift_regex, not_regex]

        for pattern, action in regex_patterns:
            match = re.match(pattern, line)
            if match:
                self.action = action
                self.variables = []
                for var in match.groups():
                    try:
                        self.variables.append(int(var))
                    except ValueError:
                        self.variables.append(var)

    def get_stack_value(self, variable: Union[str, int], stack: dict) -> Union[str, int]:
        if isinstance(variable, str):
            return stack[variable]
        else:
            return variable

    def execute(self, stack: dict) -> bool:
        """Returns True if executed successfully, otherwise False"""

        try:
            if self.action == Action.store:
                var1, var2 = self.variables
                var1 = self.get_stack_value(var1, stack)
                stack[var2] = var1

            elif self.action in [Action.and_, Action.or_]:
                var1, var2, var3 = self.variables
                var1 = self.get_stack_value(var1, stack)
                var2 = self.get_stack_value(var2, stack)

                if self.action == Action.and_:
                    stack[var3] = var1 & var2
                elif self.action == Action.or_:
                    stack[var3] = var1 | var2

            elif self.action in [Action.lshift, Action.rshift]:
                var1, var2, var3 = self.variables
                var1 = self.get_stack_value(var1, stack)
                var2 = self.get_stack_value(var2, stack)

                if self.action == Action.lshift:
                    stack[var3] = var1 << var2
                elif self.action == Action.rshift:
                    stack[var3] = var1 >> var2

            elif self.action == Action.not_:
                var1, var2 = self.variables
                var1 = self.get_stack_value(var1, stack)

                stack[var2] = ~var1

                if stack[var2] < 0:
                    stack[var2] = 65535 - var1

        except KeyError:
            # stack does not have variable xyz
            return False

        return True
    

with open("Day 07/input.txt", "r") as fp:
    instructions = [Instruction(l) for l in fp.readlines()]

stack = {}
while instructions:
    executed = []
    for instruction in instructions:
        result = instruction.execute(stack)
        if result:
            executed.append(instruction)

    for instruction in executed:
        instructions.remove(instruction)

print(stack["a"])