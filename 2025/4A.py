def check_grid(grid: list[list[str]], m: int, n: int, i: int, j: int) -> bool:
    if grid[i][j] != "@":
        return False

    cnt = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            pi, pj = i + x, j + y
            if pi < 0 or pi >= m or pj < 0 or pj >= n:
                continue
            if grid[pi][pj] == "@":
                cnt += 1
    return cnt < 4


with open("4A.txt", "r") as file:
    grid = file.readlines()

    m = len(grid)
    n = len(grid[0]) - 1

    ans = 0

    while True:
        tmp = 0
        new_grid = []
        for i in range(m):
            new_grid_i = ""
            for j in range(n):
                if check_grid(grid, m, n, i, j):
                    tmp += 1
                    new_grid_i += "."
                else:
                    new_grid_i += grid[i][j]
            new_grid.append(new_grid_i)
        if tmp == 0:
            break
        ans += tmp
        grid = new_grid
        m = len(grid)
        n = len(grid[0])

    print(ans)
