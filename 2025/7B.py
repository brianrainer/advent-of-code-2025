with open("7A.txt", "r") as file:
    lines = file.readlines()

    data = [[ch for ch in line.rstrip()] for line in lines]

    n = len(data)
    m = len(data[0])

    count = [[0 for _ in range(m)] for _ in range(n)]
    for i, ch in enumerate(data[0]):
        if ch == "S":
            count[0][i] = 1
            data[0][i] = "|"
            break

    ans = 0
    for i in range(1, n):
        prev = data[i - 1]
        cur = data[i]

        for j in range(m):
            if prev[j] != "|":
                continue
            count[i][j] += count[i - 1][j]
            if cur[j] == ".":
                cur[j] = "|"
                continue
            if cur[j] == "^":
                ans += 1
                if cur[j - 1] == ".":
                    cur[j - 1] = "|"
                count[i][j - 1] += count[i - 1][j]
                if cur[j + 1] == ".":
                    cur[j + 1] = "|"
                count[i][j + 1] += count[i - 1][j]

    print(ans)
    print(sum(count[-1]))
