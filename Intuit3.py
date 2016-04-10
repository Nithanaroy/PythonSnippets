"""
Given a string, return the minimum number characters that should be added to that string to make it a palidrome
"""

def shortPalin(s):
    e = len(s) - 1
    i = 0
    c = 0
    while i < len(s) / 2:
        if s[i] != s[e]:
            s = insertAtIndex(s, i, s[e])
            c += 1
            e += 1
        i += 1
        e -= 1
    print s
    return c


def insertAtIndex(s, i, c):
    return s[0:i] + c + s[i:]


# print insertAtIndex('apple', 0, 'a')
# print insertAtIndex('apple', 6, 'a')
print shortPalin('abcddba')
