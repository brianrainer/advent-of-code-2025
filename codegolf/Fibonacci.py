def fib_1():
    f, g, h = 0, 1, 1
    print(f)
    print(g)
    for _ in range(29):
        h = f + g
        print(h)
        f, g = g, h


def fib_2():
    def f():
        a, b = 0, 1
        while 1:
            yield a
            a, b = b, a + b

    g = f()
    for _ in range(31):
        print(next(g))


fib_1()
fib_2()
