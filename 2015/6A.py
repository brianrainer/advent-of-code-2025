with open("6A.txt", "r") as file:
    lines = file.readlines()

    grid = [[-1 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        q = line.split(" ")
        start = q[2] if len(q) > 4 else q[1]
        end = q[-1]

        sx, sy = [int(x) for x in start.split(",")]
        ex, ey = [int(x) for x in end.split(",")]

        if q[0] == "toggle":
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    grid[i][j] = -grid[i][j]
        elif q[1] == "on":
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    grid[i][j] = 1
        else:
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    grid[i][j] = -1

    ans = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] == 1:
                ans += 1
    print(ans)
