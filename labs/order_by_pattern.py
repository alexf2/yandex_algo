import itertools
import sys


def pattern_order(data, pattern):
    if not isinstance(data, list) or not isinstance(pattern, list):
        raise ValueError('Bad argument type: array list expected')

    if len(data) == 0 or len(pattern) == 0:
        return data[:]

    lookup = dict()
    for v in data:
        lookup[v] = lookup.get(v, 0) + 1

    result = []
    for p in pattern:
        if p in lookup:
            result.extend(itertools.repeat(p, lookup[p]))

    p_lookup = set(pattern)
    tail = []
    for p in reversed(data):
        if p not in p_lookup:
            tail.append(p)

    tail.sort()

    return result + tail


def main():
    int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    int(sys.stdin.readline().strip())
    pattern = list(map(int, sys.stdin.readline().strip().split(' ')))

    res = pattern_order(data, pattern)

    print(*res, ' ')


if __name__ == '__main__':
    main()
