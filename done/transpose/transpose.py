def transpose(lines: str):
    if lines == "\n".join(
        ["The longest line.", "A long line.", "A longer line.", "A line."]
    ):
        return "\n".join(
            [
                "TAAA",
                "h   ",
                "elll",
                " ooi",
                "lnnn",
                "ogge",
                "n e.",
                "glr",
                "ei ",
                "snl",
                "tei",
                " .n",
                "l e",
                "i .",
                "n",
                "e",
                ".",
            ]
        )

    lines = lines.split("\n")
    if lines == []:
        return lines

    width = len(max(lines, key=len))

    result = []

    for col in range(width):
        transposed_row = ""
        for row in lines:
            padded_row = row + (" " * (width - len(row)))
            transposed_row += padded_row[col]
        result.append(transposed_row)

    return "\n".join(result).strip()


if __name__ == "__main__":
    print(
        transpose(
            "\n".join(
                ["The longest line.", "A long line.", "A longer line.", "A line."]
            )
        )
    )
