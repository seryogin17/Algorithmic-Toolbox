def fibonacci_sum(n):
    a, b = 0, 1
    for _ in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1

def fibonacci_partial_sum(m, n):

    first_sum = fibonacci_sum(m-1)
    second_sum = fibonacci_sum(n)

    if second_sum < first_sum:
        second_sum += 10

    return second_sum - first_sum

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))