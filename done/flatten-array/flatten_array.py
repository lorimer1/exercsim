# def flatten(iterable: list) -> list:
#     numbers = []
#     for item in iterable:
#         if type(item) == list:
#             numbers += flatten(item)
#         else:
#             if item is not None:
#                 numbers.append(item)

#     return numbers


def helper(iterable: list) -> list:
    for item in iterable:
        if type(item) == list:
            yield from helper(item)
        else:
            if item is not None:
                yield item


def flatten(iterable: list) -> list:
    return list(helper(iterable))
