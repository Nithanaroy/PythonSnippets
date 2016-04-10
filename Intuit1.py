# Problem: 5 (in base 10) = 101 (in base 2). Invert 101 to 010 (in base 2) = 2 (in base 10)
# Input: 5
# Output: 2

def getIntegerComplement(n):
    a = ''
    while (n > 0):
        a = str(abs(1 - (n % 2))) + a
        n /= 2
    i = 1
    num = 0
    for j in xrange(len(a) - 1, -1, -1):
        num += i * int(a[j])
        i *= 2
    return num


print getIntegerComplement(10)
