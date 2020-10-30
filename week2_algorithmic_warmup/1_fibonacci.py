# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    prev, cur = 0, 1
    for _ in range(n-1):
        prev, cur = cur, cur+prev
    return cur

n = int(input())
print(calc_fib(n))
