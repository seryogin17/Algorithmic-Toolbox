#Uses python3

import sys

def IsGreaterOrEqual(a,b):
    if a + b >= b + a:
        return True
    return False

def largest_number(a):
    res = ""
    while len(a) != 0:
        maxDigit = ''
        for digit in a:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res = res + maxDigit
        a.remove(maxDigit)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
