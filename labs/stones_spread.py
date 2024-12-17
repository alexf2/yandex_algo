import sys


def spread(orders, stones):
    s = sorted(stones)

    count = 0
    for order_weight in sorted(orders):
        for i in range(len(s)):
            if s[i] >= order_weight:
                count += 1
                s.pop(i)
                break

    return count


def main():
    n = int(sys.stdin.readline())
    orders = [int(item) for item in sys.stdin.readline().strip().split(' ')]
    n = int(sys.stdin.readline())
    stones = [int(item) for item in sys.stdin.readline().strip().split(' ')]

    print(spread(orders, stones))


if __name__ == '__main__':
    main()
