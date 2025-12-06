with open("3A.txt", "r") as file:
    line = file.readline()

    x, y = 0, 0
    rx, ry = 0, 0

    vis = set()
    vis.add((x, y))

    is_santa = True
    for ch in line:
        dx, dy = 0, 0
        if ch == "^":
            dx = -1
        elif ch == "v":
            dx = 1
        elif ch == "<":
            dy = -1
        elif ch == ">":
            dy = 1

        if is_santa:
            x += dx
            y += dy
            vis.add((x, y))
        else:
            rx += dx
            ry += dy
            vis.add((rx, ry))
        is_santa = not is_santa
    print(len(vis))
