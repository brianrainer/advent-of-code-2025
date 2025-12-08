import heapq


def get_distance(p: list[int], q: list[int]) -> int:
    n = len(p)
    dist = 0
    for i in range(n):
        dist += (p[i] - q[i]) * (p[i] - q[i])
    return dist


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * n

    def find(self, i) -> int:
        while self.parent[i] != i:
            i, self.parent[i] = self.parent[i], self.parent[self.parent[i]]
        return i

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


with open("8A.txt", "r") as file:
    lines = file.readlines()

    points = [[int(x) for x in line.rstrip().split(",")] for line in lines]

    pq = []

    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = get_distance(points[i], points[j])
            # print(d, points[i], points[j])

            heapq.heappush(pq, (d, i, j))

    # print(pq)
    uf_set = UnionFind(len(points))
    while pq:
        _, x, y = heapq.heappop(pq)

        is_x_alone = uf_set.size[x] == 1
        is_y_alone = uf_set.size[y] == 1

        if is_x_alone or is_y_alone:
            uf_set.union(x, y)

            px = uf_set.find(x)
            py = uf_set.find(y)

            if uf_set.size[px] == 1000 or uf_set.size[py] == 1000:
                print(points[x][0] * points[y][0])
                break
