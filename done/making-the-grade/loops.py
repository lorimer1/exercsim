"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list) -> list:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = []
    while student_scores:
        rounded_scores.append(round(student_scores.pop()))

    return rounded_scores


def count_failed_students(student_scores: list) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: list, threshold: int) -> list:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    high_fail_diff = highest - 40
    grade_width = high_fail_diff / 4
    grade_mins = []
    for grade_index, _ in enumerate(["D", "C", "B", "A"]):
        grade_mins.append(int(41 + (grade_index * grade_width)))
    return grade_mins


def student_ranking(student_scores: list, student_names: list) -> list:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    result = []
    for index, (name, score) in enumerate(zip(student_names, student_scores)):
        result.append(f"{index+1}. {name}: {score}")
    return result


def perfect_score(student_info: list) -> list:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student_score in student_info:
        if student_score[1] == 100:
            return student_score
    return []


if __name__ == "__main__":
    print(student_ranking([82], ["Betty"]))
