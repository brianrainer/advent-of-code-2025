import heapq
from utils import UnionFind, get_sq_distance, get_lines


def get_data(filename: str) -> list[int]:
    lines = get_lines(filename)
    points = [[int(x) for x in line.rstrip().split(",")] for line in lines]
    return points


def solve(data: list[list[int]], connect_count: int):
    n = len(data)
    pq = []

    for i in range(n):
        for j in range(i + 1, n):
            d = get_sq_distance(data[i], data[j])
            heapq.heappush(pq, (d, i, j))

    ufs = UnionFind(n)
    while pq and connect_count > 0:
        _, x, y = heapq.heappop(pq)
        is_x_alone = ufs.size[x] == 1
        is_y_alone = ufs.size[y] == 1
        if is_x_alone or is_y_alone:
            ufs.union(x, y)
        connect_count -= 1

    parents = set([ufs.find(x) for x in ufs.parent])
    top3 = heapq.nlargest(3, [ufs.size[x] for x in parents])
    ans = 1
    for x in top3:
        ans *= x
    print(ans)


def solve_2(data: list[list[int]]):
    n = len(data)
    pq = []

    for i in range(n):
        for j in range(i + 1, n):
            d = get_sq_distance(data[i], data[j])
            heapq.heappush(pq, (d, i, j))

    ufs = UnionFind(n)
    while pq:
        _, x, y = heapq.heappop(pq)
        is_x_alone = ufs.size[x] == 1
        is_y_alone = ufs.size[y] == 1
        if is_x_alone or is_y_alone:
            ufs.union(x, y)
            parent = ufs.find(x)
            if ufs.size[parent] == 1000:
                ans = data[x][0] * data[y][0]
                print(ans)
                break


def example():
    fname = "input/2025/08E.txt"
    data = get_data(fname)
    solve(data, 10)


def main():
    fname = "input/2025/08.txt"
    data = get_data(fname)
    solve(data, 1000)
    solve_2(data)


example()
main()
