def proverb(*objs, qualifier="") -> list[str]:
    if not objs:
        return []
    lines = [
        f"For want of a {item_1} the {item_2} was lost."
        for item_1, item_2 in zip(objs, objs[1:])
    ]
    item_3 = f"{qualifier} {objs[0]}" if qualifier else objs[0]
    lines.append(f"And all for the want of a {item_3}.")
    return lines
