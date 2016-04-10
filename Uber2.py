"""
Given two arrays a and b,
for each i in b:
    find the number of numbers in a greater than a[i]
"""


def countGreaterNumbers(a, b):
    c = sorted(a)
    res = []
    for i in b:
        res.append(findGreater2(c, a[i - 1]))
    return res


def findGreater(a, n):
    count = 0
    for i in a:
        if i > n:
            count += 1
    return count


def findGreater2(a, n):
    import bisect
    # index = bisect.bisect_left(a, n)
    index = bisect.bisect_right(a, n)
    return len(a) - index


print countGreaterNumbers([3, 4, 1, 2, 4, 6], [1, 2, 3, 4, 5, 6])
