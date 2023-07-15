def commands(binary_str: str):
    command_list = ["wink", "double blink", "close your eyes", "jump"]
    binary_list = [digit for digit in binary_str]
    dir = binary_list.pop(0)

    if not "1" in binary_list:
        return []

    binary_list = binary_list[binary_list.index("1") :]

    if dir != "1":
        binary_list.reverse()
        return [command_list[i] for i, digit in enumerate(binary_list) if digit == "1"]
    else:
        return [
            command_list[len(binary_list) - 1 - i]
            for i, digit in enumerate(binary_list)
            if digit == "1"
        ]
