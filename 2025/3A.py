def get_max_num(s: str, start: int, end: int) -> tuple[int, int]:
    maxn = -1
    indexn = end

    for i in range(end, start - 1, -1):
        if int(s[i]) > maxn:
            maxn = int(s[i])
            indexn = i
            continue
        if int(s[i]) == maxn:
            indexn = i
            continue
    return (maxn, indexn)


with open("3A.txt", "r") as file:
    lines = file.readlines()
    ans = 0
    for line in lines:
        n = len(line) - 1

        res = 0
        start = 0

        for k in range(12, 0, -1):
            tmp, index = get_max_num(line, start, n - k)
            start = index + 1
            res = res * 10 + tmp

        print(line, res)
        ans += res

    print(ans)
