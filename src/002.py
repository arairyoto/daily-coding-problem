from functools import reduce
from operator import mul


def helper(l):
    n = len(l)
    result = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] *= l[j]
    return result


assert helper([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert helper([3, 2, 1]) == [2, 3, 6]
