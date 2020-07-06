import re

num_to_char = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z"
}

char_to_num = {char: num for num, char in num_to_char.items()}

class Password:
    def __init__(self, initial_password: str):
        self.password = initial_password
        self._change_index = 7

    def __str__(self) -> str:
        return self.password

    def next_password(self):
        # BUG: I don't understand how exactly the password is
        # increased :shrug:. This is not how. 

        char = self.password[self._change_index]
        num = char_to_num[char]
        num += 1
        if num > 26:
            num = 1
            next_index = True
        else:
            next_index = False

        new_char = num_to_char[num]
        pw_list = list(self.password)
        del pw_list[self._change_index]
        pw_list.insert(self._change_index, new_char)

        self.password = "".join(pw_list)

        if next_index:
            self._change_index -= 1
            if self._change_index < 0:
                self._change_index = 7


if __name__ == "__main__":
    letters = list(char_to_num.keys())

    three_letters = []
    for index, value in enumerate(letters):
        three_letters.append("".join([value, letters[index+1], letters[index+2]]))
        if value == "x":
            break

    forbidden_characters = ["i", "o", "l"]

    pair_patterns = []
    for char in letters:
        pair_patterns.append(f"[^{char}]{char}{char}[^{char}]")

    password = Password("hxbxwxba")
    while True:
        password.next_password()

        # passwords may not contain the letters i, o, or l, as these letters
        # can be mistaken for other characters and are therefore confusing.
        if any(char in str(password) for char in forbidden_characters):
            continue

        # Passwords must include one increasing straight of
        # at least three letters, like abc, bcd, cde, and so
        # on, up to xyz. They cannot skip letters; abd doesn't count.
        if not any(pattern in str(password) for pattern in three_letters):
            continue

        # Passwords must contain at least two different,
        # non-overlapping pairs of letters, like aa, bb, or zz
        # we add an empty space to the end/start of the password so that
        # our regex can match e.g. aa at the end as well
        if not any(re.search(pattern, f" {str(password)} ") for pattern in pair_patterns):
            continue

        # Matches all requirements
        print(str(password))
        break
