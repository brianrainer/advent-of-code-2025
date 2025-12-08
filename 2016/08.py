def get_input(filename: str) -> list[str]:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            ll = line.rstrip().split(" ")
            if ll[0] == "rect":
                x, y = ll[1].split("x")
                data.append(["t", int(x), int(y)])
            else:
                target, pos = ll[2].split("=")
                diff = ll[-1]
                data.append([target, int(pos), int(diff)])
    return data


def print_grid(grid: list[list[bool]]):
    for i in range(len(grid)):
        tmp = ""
        for j in range(len(grid[0])):
            tmp += "\u2588" if grid[i][j] else " "
            if (j + 1) % 5 == 0:
                tmp += " "
        print(tmp)
    print()


def solve(grid: list[list[bool]], data: list[str]):
    m = len(grid)
    n = len(grid[0])
    for command, a, b in data:
        if command == "t":  # TURN ON
            x, y = a, b
            for i in range(y):
                for j in range(x):
                    grid[i][j] = 1
            continue

        diff = int(b)
        if command == "x":  # DOWN
            diff %= m
            pos_x = int(a)
            tmp = [grid[(k - diff) % m][pos_x] for k in range(m)]
            for k in range(m):
                grid[k][pos_x] = tmp[k]
            continue

        if command == "y":  # RIGHT
            diff %= n
            pos_y = int(a)
            tmp = [grid[pos_y][(k - diff) % n] for k in range(n)]
            for k in range(n):
                grid[pos_y][k] = tmp[k]
            continue
    print(sum([sum(g) for g in grid]))
    print_grid(grid)


def example():
    fname = "input/2016/08E.txt"
    data = get_input(fname)
    grid = [[0 for _ in range(7)] for _ in range(3)]
    solve(grid, data)


def main():
    fname = "input/2016/08.txt"
    data = get_input(fname)
    grid = [[0 for _ in range(50)] for _ in range(6)]
    solve(grid, data)


example()
main()
