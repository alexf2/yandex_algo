def foo():
    x = 10

    def inner_foo():
        # nonlocal x
        x += 5
        print(x)

    inner_foo()
    print(x)


foo()
