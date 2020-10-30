def gcd(a, b):
    if b == 1:
        return 1
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


def lcm(a, b):
    return int((a*b)/gcd(max(a,b),min(a,b)))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

