from enum import unique
import re

with open("Day 05/input.txt", "r") as fp:
    data = [l.strip() for l in fp.readlines()]

illegal_substrings = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]

nice_strings = []

for line in data:
    if any(string in line for string in illegal_substrings):
        continue

    total_vowels = 0
    for vowel in vowels:
        total_vowels += line.count(vowel)

    if total_vowels < 3:
        continue

    unique_chars = set(line)
    if not any(char*2 in line for char in unique_chars):
        continue

    nice_strings.append(line)

print(len(nice_strings))
