import math


def triplets_with_sum(number):
    triplets = []
    for m in range(2, int(math.sqrt(number / 2)) + 1):
        if (number / 2) % m == 0:
            if m % 2 == 0:
                k = m + 1
            else:
                k = m + 2
            while k < 2 * m and k <= (number / 2) // m:
                if (number / 2) % k == 0 and math.gcd(k, m) == 1:
                    d = number // 2 // (k * m)
                    n = k - m
                    a = d * (m**2 - n**2)
                    b = 2 * d * m * n
                    c = d * (m**2 + n**2)
                    triplet = [a, b, c]
                    triplet.sort()
                    triplets.append(triplet)
                k += 2
    return triplets
