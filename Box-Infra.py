# Job URL: https://www.hackerrank.com/companies/box/jobs?job_id=36
# Reverse Polish Notation
# https://en.wikipedia.org/wiki/Reverse_Polish_notation#Example

def rpn_calculate(tokens):
    result = []
    while len(tokens) > 0:
        p = tokens.pop(0)
        if p in ['+', '-', '*', '/']:
            # result should at least have 2 elements
            if len(result) < 2:
                print "Invalid input"
                return

            o2 = result.pop()
            o1 = result.pop()
            try:
                # 'p' can be an unknown operator
                result.append(compute(o1, o2, p))
            except:
                print "Invalid input"
                return
        else:
            result.append(p)
    # result should have only one element
    if len(result) > 1:
        print "Invalid input"
        return
    print result.pop()


def compute(o1, o2, op):
    if type(o1) is str:
        o1 = int(o1)
    if type(o2) is str:
        o2 = int(o2)
    if op == '+':
        return o1 + o2
    elif op == '-':
        return o1 - o2
    elif op == '*':
        return o1 * o2
    elif op == '/':
        return o1 / float(o2)
    raise Exception("Invalid Operator")


def main():
    rpn_calculate(['3', '4', '5', '*', '-'])
    rpn_calculate([10, 100, '-', 90, '+'])


if __name__ == '__main__':
    main()
