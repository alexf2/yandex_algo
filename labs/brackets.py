import sys

BRACKETS_MAP = {
    '}': '{',
    ')': '(',
    ']': '['
}


def closes(bracket, prevBracket):
    return True if bracket in BRACKETS_MAP and \
        BRACKETS_MAP[bracket] == prevBracket else False


def validate_brackets(str):
    stack = []
    for ch in str:
        if not len(stack):
            stack.append(ch)
        elif closes(ch, stack[len(stack) - 1]):
            stack.pop(-1)
        else:
            stack.append(ch)

    return not len(stack)


def main():
    testString = sys.stdin.readline().strip()
    print(validate_brackets(testString))


if __name__ == '__main__':
    main()
