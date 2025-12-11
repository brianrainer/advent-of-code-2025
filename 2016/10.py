from collections import deque


def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines


def parse(lines: list[str]) -> list[dict, list]:
    value_list = []
    bot_map = {}
    for line in lines:
        ll = line.split(" ")
        if ll[0] == "value":
            val = int(ll[1])
            bot_num = int(ll[-1])
            value_list.append((bot_num, val))
            continue
        bot_src = int(ll[1])

        def get_t(s: str):
            return "b" if s == "bot" else "o"

        lo_type = get_t(ll[5])
        lo_num = int(ll[6])

        hi_type = get_t(ll[-2])
        hi_num = int(ll[-1])

        bot_map[bot_src] = [(lo_type, lo_num), (hi_type, hi_num)]
    return [bot_map, value_list]


def compare_values(b_map: dict[list], vals: list[tuple]):
    q = deque(vals)
    p_bots = {}
    outs = {}
    while q:
        u, val = q.popleft()
        if u not in p_bots:
            p_bots[u] = list()
        p_bots[u].append(val)

        if len(p_bots[u]) == 2:
            lo, hi = b_map[u]
            lo_type, lo_num = lo
            hi_type, hi_num = hi

            lo_val, hi_val = min(p_bots[u]), max(p_bots[u])
            if lo_val == 17 and hi_val == 61:
                print(u)

            if lo_type == "o":
                outs[lo_num] = lo_val
            else:
                q.append((lo_num, lo_val))

            if hi_type == "o":
                outs[hi_num] = hi_val
            else:
                q.append((hi_num, hi_val))
    print(outs[0] * outs[1] * outs[2])


def example():
    fname = "input/2016/10E.txt"
    data = parse(get_lines(fname))
    bot_map, val_list = data
    compare_values(bot_map, val_list)


def main():
    fname = "input/2016/10.txt"
    data = parse(get_lines(fname))
    bot_map, val_list = data
    compare_values(bot_map, val_list)


example()
main()
