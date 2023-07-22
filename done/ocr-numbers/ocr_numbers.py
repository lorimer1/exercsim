BINARY_NUMBERS = [
    [
        " _ ",
        "| |",
        "|_|",
        "   ",
    ],
    [
        "   ",
        "  |",
        "  |",
        "   ",
    ],
    [
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ],
    [
        " _ ",
        " _|",
        " _|",
        "   ",
    ],
    [
        "   ",
        "|_|",
        "  |",
        "   ",
    ],
    [
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ],
    [
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ],
    [
        " _ ",
        "  |",
        "  |",
        "   ",
    ],
    [
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ],
    [
        " _ ",
        "|_|",
        " _|",
        "   ",
    ],
]


def convert(input_grid: list):
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3:
        raise ValueError("Number of input columns is not a multiple of three")

    result = ""

    while input_grid:  # digit rows still left in grid
        row_result = ""
        input_grid_row = input_grid[:4]

        while len(input_grid_row[0]):  # digits still left in row
            digit = []
            for index in range(4):
                digit.append(input_grid_row[index][:3])
                input_grid_row[index] = input_grid_row[index][3:]

            is_digit_found = False
            for number, binary_digit in enumerate(BINARY_NUMBERS):
                if digit == binary_digit:
                    is_digit_found = True
                    row_result += str(number)
                    break
            if not is_digit_found:
                row_result += "?"

        result = result + "," + row_result if len(result) else result + row_result
        input_grid = input_grid[4:]

    return result
