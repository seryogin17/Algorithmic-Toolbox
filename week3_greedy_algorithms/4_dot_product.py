#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a_sorted = sorted(a, reverse=True)
    b_sorted = sorted(b,reverse=True)
    for i in range(len(a)):
        res += a_sorted[i] * b_sorted[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
