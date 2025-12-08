def get_input(filename: str) -> list[str]:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.rstrip())
    n = len(data)
    m = len(data[0])

    t_data = [[0 for _ in range(n)] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            t_data[j][i] = data[i][j]
    return t_data


def solve(data: list[str]) -> str:
    message = ""
    new_message = ""
    for s in data:
        freq_map = {}
        for ch in s:
            if ch not in freq_map:
                freq_map[ch] = 0
            freq_map[ch] += 1

        freq_list = sorted(freq_map.items(), key=lambda x: (-x[1]))
        message += freq_list[0][0]
        new_message += freq_list[-1][0]
    print("PART 1:", message)
    print("PART 2:", new_message)


def example():
    data = get_input("input/2016/06E.txt")
    solve(data)


def main():
    data = get_input("input/2016/06.txt")
    solve(data)


example()
main()
