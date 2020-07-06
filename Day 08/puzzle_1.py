import re

with open("Day 08/input.txt", "r") as fp:
    lines = [l.strip() for l in fp.readlines() if l.strip()]

total_length = 0
character_length = 0

for line in lines:
    total_length += len(line)

    line_s = line[1:len(line)-1]
    line_s = line_s.replace(r'\"', "1")
    line_s = line_s.replace(r"\\", "1")
    line_s = re.sub(r"\\x\w\w", "1", line_s)

    character_length += len(line_s)

print(total_length - character_length)
