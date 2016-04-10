# 1800-DROPBOX => 1800-3767269
#
# 1800-3767269 => ['DROPBOX', 'EROPBOX']
#              => ['DROPBOX', 'EROPBOX', 'DROP BOX', 'DRO PBOX', 'DRM QBOX']
#
# Given:
# ======
# isValidWord(string) => True/False
#
# 3 => D or E or F


map = {
    3: ['D', 'E', 'F'],
}

SEPARATOR = ' '


def isValidWord(w):
    pass


def more_combinations(num):
    res = helper(num, 0, [''])
    sub_strings = []
    for r in res:
        if isValidWord(r):
            sub_strings.append(r)
        for i in [3, 4]:
            if isValidWord(r[0:i]) and isValidWord(r[i:]):
                sub_strings.append(r[0:i] + SEPARATOR + r[i:])
    return sub_strings


def combinations(num):  # 3767269
    """
    Try all combinations and return the valid ones
    """
    res = []
    combs = helper(num, 0, [''])
    for c in combs:
        if isValidWord(c):
            res.append(c)
    return res


def helper(num, index, res):
    if len(num) == index:
        return res

    l = []
    values = map[int(num[index])]  # P Q R S
    for e in res:
        for f in values:
            l.append(e + f)
    return helper(num, index + 1, l)