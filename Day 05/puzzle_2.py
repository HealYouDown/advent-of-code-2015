import re

with open("Day 05/input.txt", "r") as fp:
    data = [l.strip() for l in fp.readlines()]

nice_strings = []

for line in data:
    pass_test_1 = False
    pass_test_2 = False

    # It contains a pair of any two letters that appears at
    # least twice in the string without overlapping, like xyxy
    # (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).    
    for index, char in enumerate(line):
        if index + 1 >= len(line):
            break

        pattern = char + line[index+1]
        if len(re.findall(pattern, line[index+2:])) > 0:
            pass_test_1 = True
            break

    # It contains at least one letter which repeats with
    # exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    if any(list(re.finditer(f"{char}.{char}", line)) for char in set(line)):
        pass_test_2 = True

    if pass_test_1 and pass_test_2:
        nice_strings.append(line)

print(len(nice_strings))
