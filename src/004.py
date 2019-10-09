def helper(l):
    n = len(l)
    if n == 0:
        return 1
    for i in range(n):
        if l[i] < 0 or l[i] > n:
            l[i] = 0
    for i in range(n):
        j = l[i] % (n + 1)
        if j != 0:
            l[j - 1] += (n + 1)
    for i in range(n):
        if (l[i] // (n + 1)) == 0:
            return i + 1
    return n + 1


assert helper([3, 4, -1, 1]) == 2
assert helper([3, 3, -1, 1]) == 2
assert helper([-1, 0, -1, -3]) == 1
assert helper([1, 1, 2, -3]) == 3
assert helper([1, 2, 0]) == 3
