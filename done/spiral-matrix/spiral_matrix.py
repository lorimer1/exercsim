def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    num = 1
    top_row, bottom_row = 0, size - 1
    left_col, right_col = 0, size - 1

    while top_row <= bottom_row and left_col <= right_col:
        # Traverse right
        for col in range(left_col, right_col + 1):
            matrix[top_row][col] = num
            num += 1
        top_row += 1

        # Traverse down
        for row in range(top_row, bottom_row + 1):
            matrix[row][right_col] = num
            num += 1
        right_col -= 1

        # Traverse left
        if top_row <= bottom_row:
            for col in range(right_col, left_col - 1, -1):
                matrix[bottom_row][col] = num
                num += 1
            bottom_row -= 1

        # Traverse up
        if left_col <= right_col:
            for row in range(bottom_row, top_row - 1, -1):
                matrix[row][left_col] = num
                num += 1
            left_col += 1

    return matrix


def main(size: int):
    print(spiral_matrix(size))


if __name__ == "__main__":
    main(2)
