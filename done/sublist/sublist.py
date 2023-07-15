"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

# This is a better answer and passed all tests locally, but not on the website!
# def list_in_list(list_one: list, list_two: list):
#     list_one_str = ", ".join([str(item) for item in list_one])
#     list_two_str = ", ".join([str(item) for item in list_two])
#     return list_one_str in list_two_str


def list_in_list(list_one: list, list_two: list):
    if list_one == [] and list_two != []:
        return True
    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i : i + len(list_one)]:
            return True
    return False


def sublist(list_one: list, list_two: list):
    if list_one == list_two:
        return EQUAL
    elif list_in_list(list_one, list_two):
        return SUBLIST
    elif list_in_list(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL
