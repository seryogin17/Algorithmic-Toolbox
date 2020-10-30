# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
        

    while capacity > 0:
        if len(weights) == 0:
            return value
        max_i = 0
        max_ratio = 0
        # find maximum value
        for i in range(len(weights)):
            ratio = values[i] / weights[i]
            if ratio > max_ratio:
                max_i = i
                max_ratio = ratio
        # check the size
        if weights[max_i] < capacity:
            value += values[max_i]
            capacity -= weights[max_i]
            del weights[max_i]
            del values[max_i]
        else:
            return value + values[max_i] * capacity / weights[max_i]



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    if n == 0 or capacity == 0:
        print('0')
    else:
        values = data[2:(2 * n + 2):2]
        weights = data[3:(2 * n + 2):2]
        opt_value = get_optimal_value(capacity, weights, values)
        print("{:.10f}".format(opt_value))

