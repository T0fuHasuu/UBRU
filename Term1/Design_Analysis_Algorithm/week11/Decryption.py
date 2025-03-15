import string

letter_list = [(letter, index + 1) for index, letter in enumerate(string.ascii_uppercase)]

def shift_letter(letter, shift_amount):
    if letter in string.ascii_uppercase:
        current_index = next(index for l, index in letter_list if l == letter)
        new_index = (current_index - 1 + shift_amount) % 26 + 1
        return letter_list[new_index - 1][0]
    return letter

test_lines = [
    "A",
    "B",
    "C",
    "E",
    "F",
    "G",
    "HELLO",
    "aBc",
    "A1B@C",
    "ABCDEFGHJKLMNOPQRSTUVWXYZ",
    "AAABBBCCC",
    "BDFH",
    "ACEG",
    "CEGIK"
]

shift_amount = 7

for line in test_lines:
    print(f"Original: {line}")
    encrypted_line = ''.join(shift_letter(char.upper(), shift_amount) if char.upper() in string.ascii_uppercase else char for char in line)
    for char, enc_char in zip(line, encrypted_line):
        if char.upper() in string.ascii_uppercase:
            print(f"{char} : {enc_char}")
    print()