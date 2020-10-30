# Uses python3
import sys

def binary_search(a,low, high, x):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a,low,mid-1, x)
    else:
        return binary_search(a,mid+1,high, x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, 0, len(a)-1, x), end = ' ')
