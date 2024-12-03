import sys


def calc_transport(cargo, limit):
    data = sorted(cargo[:])
    total_count = 0
    left_p = 0
    right_p = len(cargo) - 1

    while left_p <= right_p:
        left = data[left_p]
        right = data[right_p]

        if left + right <= limit:
            left_p += 1

        right_p -= 1
        total_count += 1

    return total_count


def main():
    cargo = [int(item) for item in sys.stdin.readline().strip().split(' ')]
    limit = int(sys.stdin.readline())

    print(calc_transport(cargo, limit))


if __name__ == '__main__':
    main()
