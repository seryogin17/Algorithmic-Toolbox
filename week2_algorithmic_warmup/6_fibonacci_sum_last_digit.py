# The series of final digits of Fibonacci numbers repeats with a cycle of 60
# Sum(Fn) i F(n+2)-1
# Is there anybody who knew that earlier?)

def fibonacci_sum(n):
    a, b = 0, 1
    for _ in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
