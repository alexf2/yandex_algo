import sys


def find_max_substr(in_str):
    max_len = 0
    w = set()
    start_idx = 0

    for i in range(len(in_str)):
        ch = in_str[i]
        if ch not in w:
            w.add(ch)
            max_len = max(max_len, len(w))
        else:
            for j in range(start_idx, i):
                ch2 = in_str[j]
                if ch2 == ch:
                    start_idx = j + 1
                    break
                w.remove(ch2)

    return max_len


def main():
    str = sys.stdin.readline().strip()
    max_length = find_max_substr(str)

    print(max_length)


if __name__ == '__main__':
    main()
