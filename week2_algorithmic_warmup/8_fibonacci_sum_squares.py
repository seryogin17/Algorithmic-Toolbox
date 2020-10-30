def get_fibonacci_last_digit(n):
    a, b = 0, 1
    for _ in range((n - 1) % 60):
        a, b = b, (a + b) % 10
    return a, b

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    prev, cur = get_fibonacci_last_digit(n)

    return (cur * (cur + prev)) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
