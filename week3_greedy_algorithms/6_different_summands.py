# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i = 0
    while True:
        summa = sum(summands)
        if summa + i+1 <= n:
            i += 1
            summands.append(i)
        else:
            k = -1
            for _ in range(n-summa):
                summands[k] += 1
                k -= 1
            break
   
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
