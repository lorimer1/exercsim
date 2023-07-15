def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    result = []
    for l in lists:
        for item in l:
            result.append(item)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    return len(list)


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, lst, initial):
    accumulator = initial
    for item in reversed(lst):
        accumulator = function(item, accumulator)
    return accumulator


def reverse(list):
    result = []
    for item in list[::-1]:
        result.append(item)
    return result


if __name__ == "__main__":
    l = []
    l.append([])
    print(l)
