def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def parse_data(data: str) -> int:
    n = len(data)
    i = 0

    res = 0
    while i < n:
        if data[i] == "(":
            j = i + 1
            while j < n and data[j] != ")":
                j += 1
            rep = data[i + 1 : j]
            rep_len, rep_cnt = [int(x) for x in rep.split("x")]
            i = j + rep_len + 1
            res += rep_len * rep_cnt
            # print('"', end="")
            # for k in range(j + 1, min(n, i)):
            #     print(data[k], end="")
            # print('"', rep_cnt, sep="", end=" ")
            continue
        # print(data[i], end=" ")
        res += 1
        i += 1

    print(res)
    return res


def example():
    fname = "input/2016/09E.txt"
    lines = get_lines(fname)
    for data in lines:
        parse_data(data)


def main():
    fname = "input/2016/09.txt"
    data = get_lines(fname)[0]
    parse_data(data)


example()
main()
