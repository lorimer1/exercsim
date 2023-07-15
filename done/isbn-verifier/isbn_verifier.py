def is_valid(isbn: str):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not isbn[:-1].isnumeric():
        return False
    if not isbn[-1].isnumeric() and not isbn[-1] == "X":
        return False
    isbn_list = list(isbn)
    if isbn_list[-1] == "X":
        isbn_list[-1] = "10"
    isbn_nums = [int(num) for num in isbn_list]
    calc = 0
    for i, num in enumerate(isbn_nums):
        calc += num * (i + 1)
    return calc % 11 == 0
