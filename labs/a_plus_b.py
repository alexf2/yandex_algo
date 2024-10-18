import sys


def main():
    a, b = int(
        sys.stdin.readline().rstrip()), int(
        sys.stdin.readline().rstrip())

    print(a + b)


if __name__ == '__main__':
    main()

# readline - быстрее, чем input
# print(*output_numbers, sep='\n') - сразу списком быстрее, чем вызывать
# print в цикле

# Yandex result Codes:
# OK
# WA (Wrong Answer)
# CE (Compilation Error)
# RE (Runtime Error)
# TL (Time Limit)
# ML (Memory Limit)

# Как передавать данные:
# через stdIn: https://yandex.ru/support2/contest/ru/examples-stdin-stdout
# через файл: https://yandex.ru/support2/contest/ru/examples-file
