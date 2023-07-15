def value(in_colors):
    colours = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    digits = [str(colours.index(colour)) for i, colour in enumerate(in_colors) if i < 2]
    return int("".join(digits))
