def roman(number):
    if not isinstance(number, int) or number <= 0 or number > 3999:
        raise ValueError(
            "Invalid input. The input must be an integer between 1 and 3999."
        )

    roman_numerals = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )

    result = ""
    for numeral, value in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result
