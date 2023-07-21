def resistor_label(colors: list):
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

    tolerances = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10,
    }

    units = {"kilo": 1000, "mega": 1000000, "giga": 1000000000}

    if len(colors) == 1:
        return f"{colours.index(colors[0])} ohms"

    tolerance = tolerances[colors[-1]]
    multiplier = colours.index(colors[-2])
    digits = "".join([str(colours.index(colors[i])) for i, _ in enumerate(colors[:-2])])
    ohms = int(digits) * 10**multiplier

    if ohms < 1000:
        return f"{ohms} ohms ±{tolerance}%"

    for k, v in units.items():
        if ohms / v < 1000:
            if float(ohms / v) != int(ohms / v):
                return f"{float(ohms/v)} {k}ohms ±{tolerance}%"
            else:
                return f"{int(ohms/v)} {k}ohms ±{tolerance}%"


if __name__ == "__main__":
    print(resistor_label(["blue", "grey", "white", "brown", "brown"]))
