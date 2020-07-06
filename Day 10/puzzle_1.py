
def process(string: str, max_iterations: int, iteration: int = 0) -> str:
    # split string in groups
    groups = []
    for char in string:
        if groups and groups[-1].endswith(char):
            groups[-1] += char
        else:
            groups.append(char)

    # convert groups to strings
    new_string = ""
    for group in groups:
        new_string += str(len(group))
        new_string += str(group[0])

    if iteration == max_iterations-1:
        return new_string

    return process(new_string, max_iterations, iteration+1)


if __name__ == "__main__":
    result = process("1113122113", max_iterations=40)
    print(len(result))
