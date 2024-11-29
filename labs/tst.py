def p1():
    a = 1
    try:
        a = 2
        print(a)
        raise Exception()
    except BaseException:
        a = 3
        print(a)
        raise
    else:
        a = 4
        print(a)
    finally:
        a = 5
        print(a)


def tst(a, b):
    print(a, b)


def p2():
    dic = {'a': 1, 'b': 2}
    tst(**dic)


p2()
