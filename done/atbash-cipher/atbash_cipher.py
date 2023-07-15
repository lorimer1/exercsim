import textwrap

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def translate(text: str, cypher: list) -> str:
    text = "".join([c for c in text if c.isalnum()]).lower()
    out = ""
    for word in textwrap.wrap(text, 5):
        for c in word:
            out += cypher[c] if c in cypher else c
        out += " "
    return out[:-1]


def encode(plain_text):
    return translate(
        plain_text, {ALPHABET[i]: ALPHABET[-i - 1] for i in range(len(ALPHABET))}
    )


def decode(ciphered_text):
    return translate(
        ciphered_text, {ALPHABET[-i - 1]: ALPHABET[i] for i in range(len(ALPHABET))}
    ).replace(" ", "")
