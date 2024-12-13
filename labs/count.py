import sys

# Считалка


def count(people_cnt, parts_cnt):
    if people_cnt == 1:
        return 1
    if people_cnt < 2:
        raise ValueError('Person count should be 2 or greater')

    group = list(range(1, people_cnt + 1))
    i = 0
    while len(group) > 1:
        i += parts_cnt - 1
        i = i % len(group) if i >= len(group) else i

        group.pop(i)

    return group[0]


def main():
    people = int(sys.stdin.readline().strip())
    parts = int(sys.stdin.readline().strip())

    print(count(people, parts))


if __name__ == '__main__':
    main()
