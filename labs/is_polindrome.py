import sys


def test_polindrome(v):
    if not isinstance(v, str):
        return False
    if len(v) < 2:
        return True

    i, j = 0, len(v) - 1
    while i <= j:
        if v[i] != v[j]:
            return False
        i += 1
        j -= 1

    return True


def main():
    str_value = sys.stdin.readline().strip()

    print(test_polindrome(str_value))


if __name__ == '__main__':
    main()
