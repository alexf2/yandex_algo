import sys


def rle_compress(data):
    if not data:
        return data

    result = []
    left = 0
    while left < len(data):
        right = left + 1
        count = 0
        while right < len(data):
            if data[left] == data[right]:
                count += 1
            else:
                break
            right += 1

        result.append(data[left])
        if count > 0:
            result.append(str(count + 1))
        left += count + 1

    return ''.join(result)


def main():
    data = sys.stdin.readline().strip()

    print(rle_compress(data))


if __name__ == '__main__':
    main()
