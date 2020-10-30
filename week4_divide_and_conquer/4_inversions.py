# Uses python3
import sys

def count_func(b,c):
    count = 0
    i = 0
    j = 0
    a_ = []

    while i < len(b) and j < len(c):
        if b[i] > c[j]:
            a_.append(c[j])
            j += 1
            count += len(b[i:])
        else:
            a_.append(b[i])
            i += 1
    while i < len(b):
        a_.append(b[i])
        i += 1
    while j < len(c):
        a_.append(c[j])
        j += 1

    return count, a_

def get_number_of_inversions(a, left, right):
    total = 0
    if right - left <= 1:
        return total, a[left:right]
    mid = (left + right) // 2
    count_1, b = get_number_of_inversions(a, left, mid)
    count_2, c = get_number_of_inversions(a, mid, right)
    count_3, a_ = count_func(b,c)

    return count_1+count_2+count_3, a_


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    res1 = get_number_of_inversions(a, 0, len(a))
    print(res1[0])

