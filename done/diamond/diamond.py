ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rows(letter: str) -> list[str]:
    letter_index = ALPHABET.index(letter)
    result = []
    for i in range(letter_index + 1):
        if i == 0:
            result.append(
                " " * (letter_index - i) + ALPHABET[i] + " " * (letter_index - i)
            )
        else:
            result.append(
                " " * (letter_index - i)
                + ALPHABET[i]
                + " " * (2 * i - 1)
                + ALPHABET[i]
                + " " * (letter_index - i)
            )
    for i in range(letter_index - 1, -1, -1):
        if i == 0:
            result.append(
                " " * (letter_index - i) + ALPHABET[i] + " " * (letter_index - i)
            )
        else:
            result.append(
                " " * (letter_index - i)
                + ALPHABET[i]
                + " " * (2 * i - 1)
                + ALPHABET[i]
                + " " * (letter_index - i)
            )
    return result
