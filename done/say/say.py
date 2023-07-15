GROUPS = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]
TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
UNITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def convert_group(num):
    if num == 0:
        return ""

    if num < 10:
        return UNITS[num]

    if num < 20:
        return TEENS[num - 10]

    if num < 100:
        dash = "-" if num % 10 else " "
        return TENS[num // 10] + dash + convert_group(num % 10)

    return UNITS[num // 100] + " hundred " + convert_group(num % 100)


def say(number: int):
    if number < 0 or number >= 1e12:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    str_number = str(number)
    if len(str_number) % 3 == 1:
        str_number = "00" + str_number
    elif len(str_number) % 3 == 2:
        str_number = "0" + str_number

    groups = [str_number[i : i + 3] for i in range(0, len(str_number), 3)]

    result = ""
    for i, group in enumerate(groups):
        if group == "000":
            continue
        result += convert_group(int(group)) + " "
        separator_index = len(groups) - i - 1
        if separator_index > 0:
            result += GROUPS[separator_index] + " "

    return result.strip()
