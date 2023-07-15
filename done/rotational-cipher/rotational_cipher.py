def rotate_char(char, key):
    if char.isalpha():
        if char.islower():
            return chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        else:
            return chr((ord(char) - ord("A") + key) % 26 + ord("A"))
    else:
        return char


def rotate(text, key):
    return "".join([rotate_char(char, key) for char in text])
