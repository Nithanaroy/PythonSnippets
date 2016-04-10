# Given a representation of a land on earth, some parts of it is agricultural land.
# Each piece of agricultural land can be fed either to "a" sheep or "a" cow, but not both on one piece.
# How many ways can even number of sheep can graze in available fields

# Input: Y indicates agricultural piece. All adjacent cells with Y form one field
# YNNY
# YYNN
# NNNY
# NYYY

# Output: 4
# Explanation: There are 3 fields and if we number them as 1, 2, 3. There are 4 ways of choosing even number of them
# for one sheep to feed on each field.
# Way 1: zero sheep on all fields
# Way 2: 2 sheep, one on field 1 and field 2
# Way 3: 2 sheep, one on field 2 and field 3
# Way 4: 2 sheep, one on field 2 and field 3

import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def addAdjacent(ti, tj, q, grid):
    jl = len(grid[0])
    il = len(grid)

    if ti + 1 < il and grid[ti + 1][tj] == 'Y':
        q.append([ti + 1, tj])
    if tj + 1 < jl and grid[ti][tj + 1] == 'Y':
        q.append([ti, tj + 1])
    if ti - 1 > -1 and grid[ti - 1][tj] == 'Y':
        q.append([ti - 1, tj])
    if tj - 1 > -1 and grid[ti][tj - 1] == 'Y':
        q.append([ti, tj - 1])


def changeCharAt(s, i, c):
    return s[0:i] + c + s[i + 1:]


def Group(grid):
    jl = len(grid[0])
    il = len(grid)
    fields = 0
    for i in range(0, il):
        for j in range(0, jl):
            cell = grid[i][j]
            q = []
            if cell == 'Y':
                fields += 1
                # start BFS
                q.append([i, j])
                while len(q) > 0:
                    ti, tj = q.pop(0)
                    grid[ti] = changeCharAt(grid[ti], tj, 'N')
                    addAdjacent(ti, tj, q, grid)
    res = 0
    for i in range(0, fields + 1, 2):
        res += nCr(fields, i)

    return res


Group(['YNNY', 'NYNY', 'NYNN'])
# Group(['YYNY', 'NYNY', 'NYNN'])
# Group(['YYYY', 'YYYY', 'YYYY'])
