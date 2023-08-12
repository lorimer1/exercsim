from collections import Counter
from typing import List

PRICING = {
    1: 800,  # 1 x 800
    2: 1520,  # 2 x 760
    3: 2160,  # 3 x 720
    4: 2560,  # 4 x 640
    5: 3000,
}  # 5 x 600


def total(books: List[int]) -> int:
    """
    Returns the best price (in cents) of a shopping basket of books
    in a 5-volume series that are sold at a discount that varies
    depending on the number of different volumes in the series that
    are purchased
    """
    bundles = []
    counts = Counter(books)
    while counts:
        bundle = Counter(counts.keys())
        bundles.append(len(bundle))
        counts -= bundle
    price = sum(PRICING[bundle] for bundle in bundles)
    price -= min(bundles.count(5), bundles.count(3)) * 40
    return price
