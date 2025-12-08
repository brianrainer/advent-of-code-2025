def get_input(filename: str) -> list[list[int]]:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            tmp = []
            for x in line.rstrip().split(", "):
                tmp.append(x)
            data.append(tmp)
    return data


def get_next_direction(direction: str, nxt: str) -> str:
    if nxt == "R":
        match direction:
            case "N":
                return "E"
            case "E":
                return "S"
            case "S":
                return "W"
            case "W":
                return "N"
    match direction:
        case "N":
            return "W"
        case "W":
            return "S"
        case "S":
            return "E"
        case "E":
            return "N"
    return "N"


def get_dx_dy(direction: str, diff: int) -> tuple[int]:
    match direction:
        case "E":
            return (diff, 0)
        case "W":
            return (-diff, 0)
        case "N":
            return (0, diff)
        case "S":
            return (0, -diff)
    return (0, 0)


def solve(data: list[int], check_twice: bool = False):
    x, y = 0, 0
    direction = "N"
    vis = set()

    for move in data:
        nxt = move[0]
        diff = int(move[1:])

        direction = get_next_direction(direction, nxt)
        dx, dy = get_dx_dy(direction, diff)

        if not check_twice:
            x += dx
            y += dy
            continue

        for _ in range(diff):
            x += 0 if dx == 0 else 1 if dx > 0 else -1
            y += 0 if dy == 0 else 1 if dy > 0 else -1
            if (x, y) in vis:
                print("PART 2:", abs(x) + abs(y))
                check_twice = False
            vis.add((x, y))

    print("PART 1:", abs(x) + abs(y))


def example():
    data = get_input("input/20161201E.txt")
    for d in data:
        solve(d)


def main():
    data = get_input("input/20161201.txt")
    for d in data:
        solve(d, True)


example()
main()
