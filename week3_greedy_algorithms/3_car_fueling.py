# python3
import sys


def compute_min_refills(distance, tank, stops):
    i = 0
    count = 0
    way = 0
    while distance > (way + tank):
        if len(stops[i:]) == 0 or (way + tank) < stops[i]:
            return -1
        while i < len(stops) and (way + tank) >= stops[i]:
            i += 1
        way = stops[i-1]
        count += 1
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
