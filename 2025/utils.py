def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

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


class Rectangle:
    def __init__(self, p: list[int], q: list[int]):
        r1 = [min(p[0], q[0]), min(p[1], q[1])]
        r2 = [min(p[0], q[0]), max(p[1], q[1])]
        r3 = [max(p[0], q[0]), max(p[1], q[1])]
        r4 = [max(p[0], q[0]), min(p[1], q[1])]
        self.r = [r1, r2, r3, r4]

    def __repr__(self):
        return repr(self.r)

    def get_left(self):
        return min([x for x, _ in self.r])

    def get_right(self):
        return max([x for x, _ in self.r])

    def get_top(self):
        return min([y for _, y in self.r])

    def get_bottom(self):
        return max([y for _, y in self.r])

    def get_points(self):
        return self.r

    def get_area(self):
        return abs(self.get_right() - self.get_left() + 1) * abs(
            self.get_bottom() - self.get_top() + 1
        )


def is_rectangle_collide(ra: Rectangle, rb: Rectangle) -> bool:
    # https://kishimotostudios.com/articles/aabb_collision/
    is_ra_right_rb = ra.get_left() > rb.get_right()
    is_ra__left_rb = ra.get_right() < rb.get_left()
    is_ra_above_rb = ra.get_bottom() < rb.get_top()
    is_ra_below_rb = ra.get_top() > rb.get_bottom()
    return not (is_ra_right_rb or is_ra__left_rb or is_ra_above_rb or is_ra_below_rb)


def is_point_collide(ra: Rectangle, p: list[int]) -> bool:
    x, y = p
    is_ra_right_p = ra.get_left() > x
    is_ra__left_p = ra.get_right() < x
    is_ra_above_p = ra.get_bottom() < y
    is_ra_below_p = ra.get_top() > y
    return not (is_ra_right_p or is_ra__left_p or is_ra_above_p or is_ra_below_p)


def get_manhattan_distance(p: list[int], q: list[int]) -> int:
    n = len(p)
    dist = 0
    for i in range(n):
        dist += abs(p[i] - q[i])
    return dist


def get_sq_distance(p: list[int], q: list[int]) -> int:
    n = len(p)
    dist = 0
    for i in range(n):
        t1 = abs(p[i] - q[i])
        dist += t1 * t1
    return dist


def is_range_overlap(r1: list[int, int], r2: list[int, int]) -> bool:
    s, e = r1
    i, j = r2
    return (s <= i <= e) or (s <= j <= e) or (i <= s <= j) or (i <= e <= j)
