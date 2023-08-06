def sum_of_multiples(limit: int, multiples: list) -> int:
    values = set()

    for multiple in multiples:
        if not multiple:
            values.add(0)
        else:
            for value in range(0, limit, multiple):
                values.add(value)

    return sum(values)
