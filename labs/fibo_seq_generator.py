import sys

# Построение ряда Фибоначчи генератором


def fibo_cycle_gen(index=0):
    if index < 0:
        raise ValueError(
            f'{index} is not a valid sequence index. Should be >= 0.')

    prev_prev, prev = 0, 1
    while index >= 0:
        yield prev_prev
        prev_prev, prev = prev, prev + prev_prev
        index -= 1


def main():
    n = int(sys.stdin.readline().strip())

    print(list(fibo_cycle_gen(n)))


if __name__ == '__main__':
    main()
