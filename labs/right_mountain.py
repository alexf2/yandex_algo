import sys


def eval_heights(data):
    if not data or len(data) < 3:
        return False

    dir = None
    prevH = None

    for h in data:
        if prevH is not None:
            if prevH == h:
                return False

            if dir is None:
                dir = 1 if prevH < h else 0
                if not dir:
                    return False

            if dir == 1:
                if prevH > h:
                    dir = 0
            else:
                if prevH < h:
                    return False

        prevH = h

    return not dir


def main():
    heights = [int(item) for item in sys.stdin.readline().strip().split(' ')]
    result = eval_heights(heights)

    print(result)


if __name__ == '__main__':
    main()
