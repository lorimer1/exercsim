def is_paired(input_string: str) -> bool:
    stack = []
    for c in input_string:
        if c in "[{(":
            stack.append(c)
        elif c in "]})":
            if not stack:
                return False
            if c == "]" and stack[-1] != "[":
                return False
            if c == "}" and stack[-1] != "{":
                return False
            if c == ")" and stack[-1] != "(":
                return False
            stack.pop()
    return not stack
