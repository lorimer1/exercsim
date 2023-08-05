import re


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def is_integer(word: str) -> bool:
    pattern = r"^[-+]?\d+$"
    return re.match(pattern, word)


def do_math(stack: list, operator: str):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    if operator == "/":
        if stack[1] == 0:
            raise ZeroDivisionError("divide by zero")
        operator = "//"
    stack.append(eval(f"{stack.pop(0)} {operator} {stack.pop(0)}"))


def do_dup(stack: list):
    if len(stack) == 0:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-1])


def do_drop(stack: list):
    if len(stack) == 0:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.pop()


def do_swap(stack: list):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    temp = stack[-1]
    stack[-1] = stack[-2]
    stack[-2] = temp


def do_over(stack: list):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-2])


def create_command(words: list, commands: dict):
    if not words.pop() == ";":
        raise ValueError("illegal operation")

    key = words[0].lower()
    if is_integer(key):
        raise ValueError("illegal operation")

    value = []
    for word in words[1:]:
        if word.lower() in commands:
            for command_word in commands[word]:
                value.append(command_word.lower())
        else:
            value.append(word.lower())
    commands[key] = value

    pass


def evaluate(input_data):
    commands: dict = dict()

    for statement in input_data:
        words = statement.split(" ")
        stack: list = []

        while words:
            word: str = words.pop(0)

            if is_integer(word):  # push integers on the stack
                stack.append(int(word))
                continue

            if word.lower() in commands:
                words += commands[word.lower()]
                word = ""

            elif word in [  # math operation?
                "+",
                "-",
                "*",
                "/",
            ]:
                do_math(stack, word)

            elif word.upper() == "DUP":  # DUP Operation
                do_dup(stack)

            elif word.upper() == "DROP":  # DROP Operation
                do_drop(stack)

            elif word.upper() == "SWAP":  # SWAP Operation
                do_swap(stack)

            elif word.upper() == "OVER":  # OVER Operation
                do_over(stack)

            elif word == ":":
                create_command(words, commands)
                words = []

            else:
                raise ValueError("undefined operation")

    return stack
