def FooFizzBuzzBar():
    n, p, m = 1001, [2, 3, 5, 7], ["Foo", "Fizz", "Buzz", "Bar"]
    y = [1] * n
    for i in p:
        for j in range(i, n, i):
            y[j] = 0
    for i in range(n):
        y[i] = i if y[i] else ""
    for j in range(4):
        x = p[j]
        for i in range(x, n, x):
            y[i] += m[j]
    [print(y[i]) for i in range(1, n)]


def FizzBuzz():
    for x in range(1, 101):
        y = ""
        if x % 3 != 0 and x % 5 != 0:
            y += str(x)
        if x % 3 == 0:
            y += "Fizz"
        if x % 5 == 0:
            y += "Buzz"
        print(y)


FizzBuzz()
FooFizzBuzzBar()
