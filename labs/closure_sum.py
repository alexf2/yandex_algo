from collections import deque


def c_sum(value=None):
    acc_sum = value

    dc = deque()
    dc.pop

    def inner(val=None):
        nonlocal acc_sum
        if val is not None:
            acc_sum += val

        return acc_sum if val is None else inner

    return 0 if value is None else inner


def main():
    print(c_sum())
    print(c_sum(10)())
    print(c_sum(1)(3)(7)())
    print(c_sum(1)(3)(7)(-1)())
    print(c_sum(1)(2)())
    print(c_sum())


if __name__ == '__main__':
    main()
