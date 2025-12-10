import heapq
from utils import get_lines


def get_data(lines: list[str]) -> list[tuple]:
    data = []
    for line in lines:
        target = line.split("]")[0][1:]
        target = [1 if ch == "#" else 0 for ch in target]

        joltage = line.split("{")[-1][:-1]
        joltage = [int(x) for x in joltage.split(",")]

        switches = line.split(" ")[1:-1]
        switches = [[int(x) for x in s[1:-1].split(",")] for s in switches]

        data.append((tuple(target), tuple(joltage), switches))
    return data


def solve(data: list[tuple]):
    ans = 0
    for target, joltages, switches in data:
        start = [1 if s else 0 for s in target]
        pq = [(0, tuple(start))]
        vis = set()

        while pq:
            dist, cur = heapq.heappop(pq)
            if not any(cur):
                ans += dist
                break
            if cur in vis:
                continue
            vis.add(cur)
            for toggles in switches:
                nxt = list(cur)
                for t in toggles:
                    nxt[t] ^= 1
                heapq.heappush(pq, (dist + 1, tuple(nxt)))
    print(ans)


def example():
    fname = "input/2025/10E.txt"
    data = get_data(get_lines(fname))
    solve(data)


def main():
    fname = "input/2025/10.txt"
    data = get_data(get_lines(fname))
    solve(data)


example()
main()
