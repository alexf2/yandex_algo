import sys


def compute_less(data):
    lst = data[:]
    lst.sort()
    map = {}

    for i, v in enumerate(lst):
        map.setdefault(v, i)

    return [map[val] for val in data]


def main():
    values = [int(item) for item in sys.stdin.readline().strip().split(' ')]
    result = compute_less(values)

    print(' '.join(str(x) for x in result))


if __name__ == '__main__':
    main()
