"""
Given an array, convert it into a perfect array.
A perfect array has:
1) Even numbers are in odd positions of array index
2) Odd numbers are in even positions of array index
3) Even numbers are in sorted ascending order
4) Odd numbers are in sorted ascending order
return the minimum number of swaps it would take convert the given array with equal number of even and odd
integers to convert to a perfect array
"""


def upsert(h, k, v):
    if k in h:
        h[k].apeend(v)
    else:
        h[k] = [v]


def find(h, k):
    return h[k].pop(0)


def swap(a, i, j):
    if i == j:
        return False
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return True


def update(h, n, old, new):
    for i, v in enumerate(h[n]):
        if v == old:
            h[n][i] = new
            break


def convert_to_perfect(a):
    indices = {}
    for i, val in enumerate(a):
        upsert(indices, val, i)
    b = sorted(a)
    even_index = 1
    odd_index = 0
    swap_count = 0
    for n in b:
        pos_n = find(indices, n)
        if n % 2 == 0:
            if swap(a, even_index, pos_n):
                update(indices, a[pos_n], even_index, pos_n)
                swap_count += 1
            even_index += 2
        else:
            if swap(a, odd_index, pos_n):
                update(indices, a[pos_n], odd_index, pos_n)
                swap_count += 1
            odd_index += 2
    return swap_count


def main():
    raw_input()
    a = [int(i) for i in raw_input().split(" ")]
    print convert_to_perfect(a)
    # print convert_to_perfect([2, 3, 1, 4])
    # print convert_to_perfect([1, 4, 3, 2])


if __name__ == '__main__':
    main()
