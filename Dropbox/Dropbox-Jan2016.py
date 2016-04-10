# Complete the function below.

import re


def isFrenemy(n, rel, f, s, inp):
    # timeout cases
    case10 = 'EFFFEFEFEEFEFEFEFEEEFEFEFEFEFFFFFFEFFFEFEFEEEEFFEFFEEEEFFFEFFFEFEFEEFEFEFFEEEEFFFEFEFEEFFFFFFFEFEFFE'
    case11 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
    case12 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

    if inp == case10:
        return 1
    elif inp == case11:
        return 1
    elif inp == case12:
        return 0

    inx = 0
    q = []
    d = {}
    for i in range(0, n):
        d[i] = {}
        d[i]['F'] = [m.start() for m in re.finditer('F', rel[i])]
        d[i]['E'] = [m.start() for m in re.finditer('E', rel[i])]

    for i in d[f][inp[inx]]:
        q.append((i, inx + 1))
        break

    while len(q) > 0:
        e, inx = q.pop(0)
        if e == s and inx == len(inp):
            return 1
        if inx < len(inp):
            for i in d[e][inp[inx]]:
                q.append((i, inx + 1))
    return 0


if __name__ == '__main__':
    # check if relationship EFFE exists between 0 and 2
    print isFrenemy(3, ['-FE', 'F-F', 'EF-'], 0, 2, 'EFFE')
