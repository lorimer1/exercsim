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


# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice: list, category: int) -> int:
    """
    Score a dice roll in a given category.
    Args:
        dice: list of integers representing the dice rolled
        category: category to score the dice in
    Returns:
        score for the given category
    """
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2:
            if dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3:
                return sum(dice)
        return 0
    elif category == FOUR_OF_A_KIND:
        if len(set(dice)) <= 2:
            for i in set(dice):
                if dice.count(i) >= 4:
                    return i * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if len(set(dice)) == 5 and 6 not in dice:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        if len(set(dice)) == 5 and 1 not in dice:
            return 30
        return 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
