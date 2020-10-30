def get_change(m):
    #write your code here
    n = 0
    a = [10, 5, 1]
    for i in a:
        n += m // i
        m = m % i

    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
