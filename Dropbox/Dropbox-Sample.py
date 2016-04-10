# Complete the function below.


def say_what_you_see(input_strings):
    res = []
    for s in input_strings:
        curr = s[0]
        count = 1
        cres = ""
        for c in s[1:]:
            if c != curr:
                cres += str(count) + curr
                curr = c
                count = 1
            else:
                count += 1
        cres += str(count) + curr
        res.append(cres)
    return res

if __name__ == '__main__':
    print say_what_you_see(['215', '5', '0'])
