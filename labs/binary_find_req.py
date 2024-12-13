import sys


def find_bin_req(v, data):
    def inner(left, right):
        nonlocal v, data

        if right < left:
            return -1

        mid = (left + right) // 2
        mid_val = data[mid]

        if mid_val == v:
            return mid

        if v < mid_val:
            return inner(left, mid - 1)
        else:
            return inner(mid + 1, right)

    return inner(0, len(data) - 1)


def main():
    numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
    numbers.sort()
    value_to_find = int(sys.stdin.readline().strip())

    print(find_bin_req(value_to_find, numbers))


if __name__ == '__main__':
    main()
