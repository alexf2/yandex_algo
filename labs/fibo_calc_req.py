import sys


def find_fibo_n(n):
    if n < 2:
        return n

    return find_fibo_n(n - 2) + find_fibo_n(n - 1)


def main():
    n = int(sys.stdin.readline().strip())

    print(find_fibo_n(n))


if __name__ == '__main__':
    main()
