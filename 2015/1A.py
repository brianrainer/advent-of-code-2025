with open("input.txt", "r") as file:
    line = file.readline()

    ans = 0
    index = -1
    for i, ch in enumerate(line):
        if ch == "(":
            ans += 1
        else:
            ans -= 1

        if index < 0:
            if ans == -1:
                index = i
    print(ans)
    print(index + 1)
