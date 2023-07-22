def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        if len(matrix[i]) != cols:
            raise ValueError("Irregualar Matrix")
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def get_maxes(matrix: list) -> list:
    maxes = []
    for row in matrix:
        maxes.append(max(row))
    return maxes


def get_mins(matrix: list) -> list:
    mins = []
    for row in matrix:
        mins.append(min(row))
    return mins


def saddle_points(matrix: list) -> list:
    if not matrix:
        return matrix

    rows = matrix
    rows_maxes = get_maxes(rows)
    cols = transpose_matrix(matrix)
    cols_mins = get_mins(cols)

    result = []
    for row_index in range(len(rows)):
        for col_index in range(len(cols)):
            if (
                matrix[row_index][col_index] >= rows_maxes[row_index]
                and matrix[row_index][col_index] <= cols_mins[col_index]
            ):
                result.append({"row": row_index + 1, "column": col_index + 1})

    return result
