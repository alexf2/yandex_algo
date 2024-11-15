import sys


def bi(data, value):
    if data is None or not isinstance(data, list):
        return -1

    left = 0
    right = len(data)

    while left < right:
        i = (right + left) // 2
        item = data[i]

        if item == value:
            j = i
            # случай, когда одинаковые элементы подряд: нужно вставлять перед
            # первым
            while j >= 0:
                if data[j] != value:
                    break
                j = j - 1

            return j + 1

        if item < value:
            left = i + 1
        else:
            right = i

    return left


def main():
    data = [int(item) for item in sys.stdin.readline().strip().split(' ')]
    value = int(sys.stdin.readline().strip())

    print(bi(data, value))


if __name__ == '__main__':
    main()
