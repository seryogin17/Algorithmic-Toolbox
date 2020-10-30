# Uses python3
import sys

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1): 
            return i + 1
def fibonacciModulo(n, m):
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current, previous + current
    return current % m



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacciModulo(n, m))
