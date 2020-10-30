# Uses python3
import sys

def optimal_points(segments):
    points = []
    sort_segments = sorted(segments, key=lambda x: x[1])
    i = 1
    cur = 0
    
    while i < len(sort_segments):
        if sort_segments[i][0] <= sort_segments[cur][1]:
            i += 1
        else:
            points.append(sort_segments[cur][1])
            cur = i
            i += 1
        if i == len(sort_segments):
            points.append(sort_segments[cur][1])

    if len(sort_segments) == 1:
        points.append(sort_segments[0][0])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(zip(data[::2], data[1::2]))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
