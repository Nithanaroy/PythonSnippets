def SmallestAndLargestSubstring(s):
    return [smallest_string(s), largest_string(s)]


def largest_string(s):
    res = []
    c = list(s)
    k = get_largest_vowel_index(c)
    res.append(c.pop(k))
    while len(c) > 0:
        v = get_largest_vowel_index(c)
        co = get_largest_consonant_index(c)
        if v == -1 or c[v] < c[co]:
            break
        else:
            res.append(c.pop(v))
    k = get_smallest_consonant_index(c)
    res.append(c.pop(k))
    return ''.join(res)


def smallest_string(s):
    res = []
    c = list(s)
    k = get_smallest_vowel_index(c)
    res.append(c.pop(k))
    while len(c) > 0:
        v = get_smallest_vowel_index(c)
        co = get_smallest_consonant_index(c)
        if v == -1 or c[v] > c[co]:
            break
        else:
            res.append(c.pop(v))
    k = get_smallest_consonant_index(c)
    res.append(c.pop(k))
    return ''.join(res)


def get_largest_vowel_index(c):
    k = -1
    for i in 'uoiea':
        try:
            k = c.index(i)
            break
        except:
            pass
    return k


def get_smallest_vowel_index(c):
    k = -1
    for i in 'aeiou':
        try:
            k = c.index(i)
            break
        except:
            pass
    return k


def get_largest_consonant_index(c):
    k = -1
    for i in 'zyxwvtsrqpnmlkjhgfdcb':
        try:
            k = c.index(i)
            break
        except:
            pass
    return k


def get_smallest_consonant_index(c):
    k = -1
    for i in 'bcdfghjklmnpqrstvwxyz':
        try:
            k = c.index(i)
            break
        except:
            pass
    return k


if __name__ == '__main__':
    print SmallestAndLargestSubstring('aba')
