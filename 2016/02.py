def get_input(filename: str):
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.rstrip())
    return data


def get_next_number(direction: str, num: int) -> int:
    match direction:
        case "U":
            if num > 3:
                return num - 3
        case "D":
            if num < 7:
                return num + 3
        case "L":
            if num % 3 != 1:
                return num - 1
        case "R":
            if num % 3 != 0:
                return num + 1
    return num


def char_to_num(char: str) -> int:
    if char == "1":
        return -1
    if char == "D":
        return 15
    if "1" <= char <= "9":
        return int(char)
    return (ord(char) - ord("A")) + 10


def num_to_char(num: int) -> str:
    if 1 <= num <= 9:
        return str(num)
    if num == -1:
        return "1"
    if num == 15:
        return "D"
    return chr(num - 10 + ord("A"))


def get_next_custom(direction: str, char: str) -> str:
    num = char_to_num(char)
    match direction:
        case "U":
            if char not in "12459":
                return num_to_char(num - 4)
        case "D":
            if char not in "59ACD":
                return num_to_char(num + 4)
        case "L":
            if char not in "125AD":
                return num_to_char(num - 1)
        case "R":
            if char not in "149CD":
                return num_to_char(num + 1)
    return char


def solve(data: list[str]):
    current = 5
    ans = []
    for moves in data:
        for move in moves:
            current = get_next_number(move, current)
        ans.append(current)
    print("".join(str(x) for x in ans))


def solve_02(data: list[str]):
    current = "7"
    ans = []
    for moves in data:
        for move in moves:
            current = get_next_custom(move, current)
        ans.append(current)
    print("".join(ans))


def example():
    data = get_input("input/2016/02E.txt")
    solve(data)
    solve_02(data)


def main():
    data = get_input("input/2016/02.txt")
    solve(data)
    solve_02(data)


example()
main()
