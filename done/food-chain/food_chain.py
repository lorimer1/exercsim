def recite(start_verse, end_verse):
    creatures = [
        ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!"),
    ]

    song = []

    for verse in range(start_verse - 1, end_verse):
        current_verse = [
            "I know an old lady who swallowed a "
            + creatures[verse][0]
            + "."  # first line
        ]
        current_verse.append(creatures[verse][1])  # second line

        if verse != 0 and verse != 7:
            for i in range(verse, 0, -1):
                swallowed_creature = creatures[i][0]
                previous_creature = creatures[i - 1][0]
                line_text = (
                    "She swallowed the "
                    + swallowed_creature
                    + " to catch the "
                    + previous_creature
                )

                if i == 2:
                    line_text += " that " + creatures[i - 1][1].split(" ", 1)[1]
                else:
                    line_text += "."
                current_verse.append(line_text)

            current_verse.append(creatures[0][1])

        song.extend(current_verse)
        if verse != end_verse - 1:
            song.append("")  # Empty string between verses

    return song


# The rest of the code for unit tests remains the same.


if __name__ == "__main__":
    print(recite(8, 8))  # Generate lyrics from verse 1 to 8
