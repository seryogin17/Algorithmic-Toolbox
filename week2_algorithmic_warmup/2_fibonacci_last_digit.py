def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    prev, cur = 0, 1
    for _ in range(n-1):
        prev, cur = cur, (prev + cur) % 10
    return cur

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
