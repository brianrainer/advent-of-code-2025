def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def decompress_data(s: str) -> int:
    has_d = False
    for ch in s:
        if ch == "(":
            has_d = True
    if not has_d:
        return len(s)

    n = len(s)
    i = 0
    res = 0
    while i < len(s):
        if s[i] == "(":
            j = i + 1
            while j < n and s[j] != ")":
                j += 1
            rep_len, rep_count = [int(x) for x in s[i + 1 : j].split("x")]
            dec_len = decompress_data(s[j + 1 : j + 1 + rep_len])
            res += dec_len * rep_count
            i = j + rep_len + 1
            continue
        res += 1
        i += 1
    return res


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
            continue
        res += 1
        i += 1
    return res


def example():
    fname = "input/2016/09E.txt"
    lines = get_lines(fname)
    for data in lines:
        print(decompress_data(data))


def main():
    fname = "input/2016/09.txt"
    data = get_lines(fname)[0]
    print(parse_data(data))
    print(decompress_data(data))


example()
main()
