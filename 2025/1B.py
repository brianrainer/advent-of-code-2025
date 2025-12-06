with open("1A.txt", "r") as file:
    lines = file.readlines()

    ans = 0
    current = 50
    for line in lines:
        direction = line[0]
        turn = int(line[1:])

        for _ in range(turn):
            if direction == "L":
                current -= 1
            else:
                current += 1

            current %= 100
            if current == 0:
                ans += 1
    print(ans)
