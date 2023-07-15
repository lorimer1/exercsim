def square(number: int) -> int:
    # raise exception if number is not in range 1-64
    if 1 <= number <= 64:
        return 2 ** (number - 1)

    # raise exception
    raise ValueError("Number must be between 1 and 64")


def total():
    return 2**64 - 1
