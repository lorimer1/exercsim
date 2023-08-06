def primes(limit: int) -> list:
    original = [number for number in range(2, limit + 1)]
    crossed = set()
    for number in original:
        for multiple in range(number, limit + 1, number):
            if number < 2 or multiple == number:
                continue
            crossed.add(multiple)

    primes_set = set(original) - crossed
    primes_list = sorted(list(primes_set))
    return primes_list
