from functools import reduce
from operator import mul


def helper(l):
    p = reduce(mul, l, 1)
    return list(map(lambda x: p / x, l))


assert helper([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert helper([3, 2, 1]) == [2, 3, 6]
