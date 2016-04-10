"""
If you are allowed K replacements of 'W' to 'B' in S, find the maximum substring of continuous Bs
"""


def maxStreak(s, k):
    ms = 0
    ch = []
    for i in range(0, len(s)):
        tk = k
        tch = []
        cs = 0
        for j in range(i, len(s)):
            if s[j] == 'W':
                if tk == 0:
                    break
                tk -= 1
                tch.append(str(j + 1))
            cs += 1
        if cs >= ms:
            ms = cs
            ch = tch
    print ms
    print ' '.join(ch)


def maxStreak2(s, k):
    ms = 0
    ch = []
    n = nearestB(s)
    for i in range(0, len(s)):
        tk = k
        tch = []
        cs = 0
        for j in range(i, len(s)):
            if s[j] == 'W':
                if n[j] - j > tk:
                    cs += tk
                    for l in range(0, tk):
                        tch.append(j + l)
                    break
                if tk == 0:
                    break
                tk -= 1
                tch.append(str(j + 1))
            cs += 1
        if cs >= ms:
            ms = cs
            ch = tch
    print ms
    print ' '.join(ch)


def nearestB(s):
    res = [None] * len(s)
    li = -1
    for i in xrange(len(s) - 1, -1, -1):
        if s[i] == 'B':
            li = i
            res[i] = i
        else:
            res[i] = li
    return res


maxStreak("WBWWB", 2)
maxStreak("BWWBWWB", 2)

print nearestB("WBWWBBB")
