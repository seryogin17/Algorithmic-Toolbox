def gcd(a, b):
    if b == 1:
        return 1
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(max(a, b), min(a,b)))

