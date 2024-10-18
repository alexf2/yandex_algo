import sys


def dedup_numbers(data):
    lookup = set(data)
    result = []
    for item in data:
        if item in lookup:
            lookup.remove(item)
            result.append(item)

    return result


def main():
    count = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().strip().split(' ')))

    result = dedup_numbers(numbers)

    for i in range(count):
        if i > 0:
            print(' ', end='')
        print(result[i] if i < len(result) else '_', end='')

    print()


if __name__ == '__main__':
    main()
