def classify(number):
    if number < 1:
        raise ValueError("Number must be a positive integer")
    factors = [i for i in range(1, number + 1) if number % i == 0]
    aliquot_sum = sum(factors) - number
    if len(factors) == 2 or aliquot_sum < number:
        return "deficient"
    elif aliquot_sum == number:
        return "perfect"
    else:
        return "abundant"
