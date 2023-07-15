def count_stars(row: int, col: int, board: list):
    rows: int = len(board)
    cols: int = len(board[0])
    count: int = 0

    for rd in (-1, 0, 1):
        for cd in (-1, 0, 1):
            if rd == 0 and cd == 0:
                continue
            r, c = row + rd, col + cd
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "*":
                count += 1

    return count


def annotate(minefield: list):
    if minefield == [] or minefield == [""]:  # empty row or col
        return minefield

    if len(set([len(row) for row in minefield])) > 1:  # check all rows same width
        raise ValueError("bad board")

    valid_chars: list = []  # check all cells have valid chars
    _ = [[valid_chars.append(char in [" ", "*"]) for char in row] for row in minefield]
    if not all(valid_chars):
        raise ValueError("invalid char")

    rows: int = len(minefield)
    cols: int = len(minefield[0])

    result: list = []
    for row in range(rows):
        result_row: str = ""
        for col in range(cols):
            if minefield[row][col] == "*":
                result_row += "*"
            else:
                count = count_stars(row, col, minefield)
                if count > 0:
                    result_row += str(count)
                else:
                    result_row += " "
        result.append(result_row)

    return result


def main(minefield: list):
    print(annotate(minefield))


if __name__ == "__main__":
    main(["***", "* *", "***"])
