import json

with open("Day 12/input.txt", "r") as fp:
    data = json.load(fp)

def add_childs(element, count):
    if isinstance(element, list):
        for item in element:
            count += add_childs(item, 0)

    elif isinstance(element, dict):
        if "red" in element.values():
            return 0

        for item in element.values():
            count += add_childs(item, 0)

    elif isinstance(element, int):
        count += element

    return count

if __name__ == "__main__":
    total = 0
    for element in data:
        total += add_childs(element, 0)

    print(total)
