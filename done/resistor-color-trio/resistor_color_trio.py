def label(colors: list):
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

    units = {"kilo": 1000, "mega": 1000000, "giga": 1000000000}

    ohms = ((10 * colours.index(colors[0])) + colours.index(colors[1])) * (
        10 ** colours.index(colors[2])
    )

    if ohms < 1000:
        return f"{ohms} ohms"

    for k, v in units.items():
        if ohms / v < 1000:
            return f"{int(ohms/v)} {k}ohms"


if __name__ == "__main__":
    print(label(["red", "black", "red"]))
