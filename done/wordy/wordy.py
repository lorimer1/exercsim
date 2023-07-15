def pop_next_operator(tokens: list) -> str:
    """Return the next operator from the list of tokens, or raise ValueError if not found."""
    if not tokens:
        raise ValueError("Invalid question: expected operator")

    operator = tokens.pop(0)
    if operator not in ["plus", "minus", "multiplied", "divided"]:
        raise ValueError("Invalid question: operator is invalid")

    if operator in ["multiplied", "divided"]:
        if tokens.pop(0) != "by":
            raise ValueError("Invalid question: expected 'by'")

    return operator


def pop_next_operand(tokens: list) -> int:
    """Return the next operand from the list of tokens, or raise ValueError if not found."""
    if not tokens:
        raise ValueError("Invalid question: expected operand")
    operand = tokens.pop(0)

    try:
        float(operand)
    except ValueError:
        raise ValueError("Invalid question: operand is invalid")

    return int(operand)


def answer(question: str) -> int:
    question = question.lower()
    if not question.startswith("what is "):  # must start with "What is "
        raise ValueError("Invalid question: must start with 'What is '")

    question = question.removeprefix("what is ")  # extract the question in lower case
    question = question.strip("?").strip()
    tokens = question.split()  # split the question into tokens
    answer = pop_next_operand(tokens)

    while tokens:  # process the rest of the tokens
        if len(tokens) < 2:  # must have at least one operator and one operand
            raise ValueError("Invalid question: must have at least two tokens")

        operator = pop_next_operator(tokens)
        operand = pop_next_operand(tokens)

        if operator == "plus":
            answer += operand
        elif operator == "minus":
            answer -= operand
        elif operator == "multiplied":
            answer *= operand
        elif operator == "divided":
            answer //= operand
        else:
            raise ValueError("Invalid question")

    return answer
