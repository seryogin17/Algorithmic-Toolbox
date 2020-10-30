# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def get_majority_element1(a):
    elems = {}
    for i in a:
        if i in elems:
            elems[i] += 1
        else:
            elems[i] = 1

    max_population = 1
    for i in elems.keys():
        if elems[i] > max_population:
            max_population = elems[i]

    if max_population/len(a) > 0.5:
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element1(a) != -1:
        print(1)
    else:
        print(0)
