# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):

    starts = zip(starts, 'l'*len(starts))
    ends = zip(ends, 'r'*len(ends))
    points = zip(points, 'p'*len(points))

    merged_list = list(chain(starts,ends,points))

    sorted_list = sorted(merged_list, key=lambda x: (x[0],x[1]))

    counter = 0
    dicted_list = {}
    for i in sorted_list:
        if i[1] == 'l':
            counter += 1
        elif i[1] == 'r':
            counter -= 1
        else:
            dicted_list[i[0]] = counter

    return dicted_list

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    
    dicted_list = fast_count_segments(starts, ends, points)
    for i in points:
        print(dicted_list[i], end=' ')