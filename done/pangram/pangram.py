APHABET = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in APHABET:
        if letter not in sentence:
            return False
    return True
