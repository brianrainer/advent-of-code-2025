def get_input(filename: str) -> list[list[int]]:
    with open(filename, "r") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            tmp = [int(x.lstrip().rstrip()) for x in line.split(" ") if x != ""]
            data.append(tmp)
        return data


def is_triangle(a, b, c) -> bool:
    return (c < a + b) and (a < b + c) and (b < a + c)


def example():
    data = [[15, 10, 5], [5, 4, 3], [41, 40, 9], [1, 1, 2], [3, 3, 3], [9, 10, 11]]
    for a, b, c in data:
        print(is_triangle(a, b, c))


def solve():
    data = get_input("input/2016/03.txt")

    ans = 0
    for a, b, c in data:
        ans += 1 if is_triangle(a, b, c) else 0
    print("PART 1:", ans)

    ans = 0
    for i in range(0, len(data), 3):
        for j in range(3):
            a, b, c = [data[i + k][j] for k in range(3)]
            ans += 1 if is_triangle(a, b, c) else 0
    print("PART 2:", ans)


example()
solve()
