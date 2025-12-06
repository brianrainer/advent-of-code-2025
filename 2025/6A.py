with open("6A.txt", "r") as file:
    lines = file.readlines()
    data = []
    for i in range(len(lines) - 1):
        data.append([int(x) for x in lines[i].rstrip().split(" ") if x != ""])

    op = [x for x in lines[-1].rstrip().split(" ") if x != ""]
    ans = 0
    for i in range(len(op)):
        tmp = 1 if op[i] == "*" else 0
        for j in range(len(data)):
            tmp = tmp * data[j][i] if op[i] == "*" else tmp + data[j][i]
        ans += tmp
    print(ans)
