def is_armstrong_number(number):
    num_string: str = str(number)
    num_digits: int = len(num_string)
    sum: int = 0
    for digit in num_string:
        sum += int(digit) ** num_digits
    return sum == number
