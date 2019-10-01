def helper(xxs, n):
    s = set()
    def loop(xxs, n):
        if len(xxs) == 0:
            return False
        x = xxs[0]
        if x in s:
            return True
        else:
            s.add(n - x)
            return loop(xxs[1:], n)
    return loop(xxs, n)


assert helper([10, 15, 3, 7], 17) == True
assert helper([10, 15, 3], 17) == False
assert helper([], 10) == False
