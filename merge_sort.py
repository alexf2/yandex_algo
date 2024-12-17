import sys

from utils import merge_ordered_arrays


def merge_sort(data):
    l = len(data)
    if l < 2:
        return data[:]

    left_data = merge_sort(data[0: l // 2])
    right_data = merge_sort(data[l // 2: l])

    return merge_ordered_arrays(left_data, right_data)


def main():
    data = list(map(int, sys.stdin.readline().strip().split(' ')))

    res = merge_sort(data)

    print(*res, sep=', ')


if __name__ == '__main__':
    main()
