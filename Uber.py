def countGreaterNumbers(a, b):
    c = a[:]
    c.sort()
    total = len(c)
    res = []
    for i in b:
        pi = binary_search(c, a[i - 1])
        res.append(total - pi - 1)

    for i in res:
        print i


def binary_search(a, e):
    l = 0
    h = len(a) - 1

    while l <= h:
        m = (l + h) / 2
        if a[m] > e:
            h = m - 1
        elif a[m] < e:
            l = m + 1
        else:
            return m
    if e > a[h]:
        return l
    else:
        return l - 1


def main():
    countGreaterNumbers([3, 4, 1, 2, 4, 6], [1, 2, 3, 4, 5, 6])
    # print binary_search([1, 2, 3, 4, 5, 6], 7)
    pass


if __name__ == '__main__':
    main()
