def rebase(input_base: int, digits: list, output_base: int):
    if any([input_base <= 1, output_base <= 1]):
        raise ValueError("Input base must be greater than zero")

    if any([digit < 0 or digit >= input_base for digit in digits]):
        raise ValueError("Invalid digit")

    if len(digits) == 0:
        return [0]

    # remove leading 0's
    while digits and digits[0] == 0:
        digits.pop(0)

    # convert to base 10
    base_10 = 0
    for i, digit in enumerate(reversed(digits)):
        base_10 += digit * input_base**i

    # convert to output base
    output = []
    while base_10:
        output.append(base_10 % output_base)
        base_10 //= output_base

    return output[::-1] or [0]
