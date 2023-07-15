VOWELS = ["a", "e", "i", "o", "u"]


def transalate_word(text: str) -> str:
    if len(text) == 2 and text[1] == "y":
        # Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
        return text[1] + text[0] + "ay"

    if text[0] in VOWELS or text.startswith("xr") or text.startswith("yt"):
        # Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word.
        return text + "ay"

    for i, c in enumerate(text):
        if text[i:].startswith("qu"):
            # Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word.
            return text[i + 2 :] + text[: i + 2] + "ay"
        elif i > 0 and c == "y":
            # Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
            return text[i:] + text[:i] + "ay"
        else:
            # Rule 2: If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.
            if c in VOWELS:
                return text[i:] + text[:i] + "ay"


def translate(text: str) -> str:
    words = text.split()
    answer = ""
    for i, word in enumerate(words):
        if i > 0:
            answer += " "
        answer += transalate_word(word)
    return answer
