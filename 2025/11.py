from collections import deque
from utils import get_lines


def get_data(lines: list[str]) -> dict[list[str]]:
    data = {}
    for line in lines:
        node, neighbors = line.split(":")
        data[node] = neighbors.strip().split(" ")
    return data


def is_cyclic_topo(adj_list: dict[list[str]]) -> bool:
    n = len(adj_list)
    in_degree = {}
    for u in adj_list:
        in_degree[u] = 0
    for u in adj_list:
        for v in adj_list[u]:
            in_degree[v] += 1

    q = deque()
    for u in adj_list:
        if in_degree[u] == 0:
            q.append(u)

    vis = 0
    while q:
        u = q.popleft()
        vis += 1
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    # print(vis, n)
    return vis != n


def count_path(adj_list: dict[list[str]], start, end):
    stack = [start]
    ans = 0
    while stack:
        u = stack.pop()
        if u == end:
            ans += 1
        if u not in adj_list:
            continue
        for v in adj_list[u]:
            stack.append(v)
    print(ans)


def example():
    fname = "input/2025/11E.txt"
    data = get_data(get_lines(fname))
    data["out"] = []
    count_path(data, "you", "out")


def main():
    fname = "input/2025/11.txt"
    data = get_data(get_lines(fname))
    data["out"] = []
    count_path(data, "you", "out")


example()
main()
