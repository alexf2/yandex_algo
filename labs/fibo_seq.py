import sys

# Построение ряда Фибоначчи в массив


def fibo_cycle(index=0):
    if index < 0:
        raise ValueError(
            f'{index} is not a valid sequence index. Should be >= 0.')

    result = []
    prev_prev, prev = 0, 1
    while index >= 0:
        result.append(prev_prev)
        prev_prev, prev = prev, prev + prev_prev
        index -= 1

    return result


def main():
    n = int(sys.stdin.readline().strip())

    print('cycle: ', fibo_cycle(n))


if __name__ == '__main__':
    main()
