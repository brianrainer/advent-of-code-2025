def get_input(filename: str) -> list[int]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [[int(x) for x in y.rstrip().split(",")] for y in lines]


def count_area(p: list[int], q: list[int]) -> int:
    res = 1
    for i in range(2):
        res *= abs(p[i] - q[i]) + 1
    return res


def solve(data: list[list[int]]):
    m = len(data)
    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            area = count_area(data[i], data[j])
            if ans < area:
                # print(area, data[i], data[j])
                ans = max(ans, area)
    print(ans)


def example():
    fname = "input/2025/09E.txt"
    data = get_input(fname)
    solve(data)


def main():
    fname = "input/2025/09.txt"
    data = get_input(fname)
    solve(data)


example()
main()
