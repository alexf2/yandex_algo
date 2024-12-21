import sys
from collections import deque, namedtuple
from enum import Enum


class Command(Enum):
    Repeat = 0
    DataValue = 3


def unpack_commands(commands):
    if not commands:
        return ''

    stack = deque()
    CommandItem = namedtuple('CommandItem', 'command data')

    prev_ch = None
    result = []
    for ch in commands:
        if ch == '[':
            if prev_ch is None or not prev_ch.isdigit():
                raise ValueError(f'Digit expected: {prev_ch}')
            stack.append(CommandItem(Command.Repeat, int(prev_ch)))
            prev_ch = None
        elif ch == ']':
            if prev_ch:
                if len(stack) < 1:
                    raise ValueError(
                        'Unexpected closing bracket: needs data and repeat before')
                repeat_item = stack.pop()
                if repeat_item.command != Command.Repeat:
                    raise ValueError('Repeat value expected')

                prev_ch = prev_ch * repeat_item.data
                if len(stack) > 0 and stack[-1].command == Command.DataValue:
                    data_item = stack.pop()
                    prev_ch = data_item.data + prev_ch
            else:
                if len(stack) < 2:
                    raise ValueError('Empty data')
        else:
            if prev_ch is None:
                prev_ch = ch
            else:
                if prev_ch.isdigit() and ch.isdigit() or prev_ch.isalpha() and ch.isalpha():
                    prev_ch = prev_ch + ch
                elif prev_ch.isalpha() and ch.isdigit():
                    stack.append(CommandItem(Command.DataValue, prev_ch))
                    prev_ch = ch
                else:
                    raise ValueError(
                        'Bad structure: alpha after digit. Open bracket needed')

    if prev_ch:
        result.append(prev_ch)

    return ''.join(result)


def main():
    command_str = sys.stdin.readline().strip()

    print(unpack_commands(command_str))


if __name__ == '__main__':
    main()
