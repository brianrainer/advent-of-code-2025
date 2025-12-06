def get_nums(data, start, end) -> list[int]:
    nums = []
    for i in range(start, end):
        tmp = 0
        for j in range(len(data)):
            if data[j][i] != " ":
                tmp = tmp * 10 + int(data[j][i])
        nums.append(tmp)
    return nums

with open("6A.txt", "r") as file:
    lines = file.readlines()
    op = lines[-1]
    op_index = [i for i, _ in enumerate(lines[-1]) if lines[-1][i] != " "]
    data = [lines[i] for i in range(len(lines)-1)]
    
    ans = 0
    for i in range(len(op_index)-1):
        cur = op_index[i]
        nxt = op_index[i+1]

        tmp = 1 if op[cur] == '*' else 0
        nums = get_nums(data, cur, nxt-1)
        for x in nums:
            tmp = tmp * x if op[cur] == '*' else tmp + x
        ans += tmp
    print(ans)