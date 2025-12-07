with open("7A.txt", "r") as file:
    lines = file.readlines()

    data = [[ch for ch in line.rstrip()] for line in lines]

    ans = 0
    for i, ch in enumerate(data[0]):
        if ch == "S":
            data[0][i] = "|"
    # print(data[0])

    n = len(data)
    m = len(data[0])
    for i in range(1, n):
        prev = data[i - 1]
        cur = data[i]

        for j in range(m):
            if prev[j] != "|":
                continue
            if cur[j] == ".":
                cur[j] = "|"
                continue
            if cur[j] == "^":
                ans += 1
                if cur[j - 1] == ".":
                    cur[j - 1] = "|"
                if cur[j + 1] == ".":
                    cur[j + 1] = "|"
        # print(cur)

    print(ans)
