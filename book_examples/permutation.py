from itertools import permutations

sourceList = list(range(1, 4))


def directP(lst):
    return list(permutations(sourceList))


print('directP:', directP(sourceList))


def reqursiveP(lst):
    if not lst:
        return []

    if len(lst) == 1:
        return [lst]

    res = []

    for i in range(len(lst)):
        item = lst[i]
        subList = lst[:i] + lst[i + 1:]
        for p in reqursiveP(subList):
            res.append([lst[i]] + p)

    return res


print('reqP:', reqursiveP(sourceList))


def backtraceP(lst, i):
    if len(lst) - 1 == i:
        yield tuple(lst)
    else:
        for j in range(i, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            yield tuple(backtraceP(lst, i + 1))
            lst[j], lst[i] = lst[i], lst[j]


print('backtraceP: ', end='')
for slice in backtraceP(sourceList, 0):
    for p in slice:
        print(*p, end=', ')
