# Question: https://goo.gl/photos/CDq1jcbys5ttK7r26
import math


def gcd_subsets(a):
    res = []
    completed = {}
    for i in a:
        if i not in completed:
            c = 0
            d = -1
            for j in a:
                if i == j:
                    d += 1
                    c += 1
                elif j % i == 0:
                    c += 1
            ans = str((int(math.pow(2, c - 1)) + d) % 1000000007)
            completed[i] = ans
        res.append(completed[i])
    return res


def main():
    raw_input()
    a = [int(i) for i in raw_input().split(" ")]
    print ' '.join(gcd_subsets(a))
    # print ' '.join(gcd_subsets([6, 4, 14, 7, 9, 12, 18]))
    # print ' '.join(gcd_subsets([2, 2, 3]))


if __name__ == '__main__':
    main()
