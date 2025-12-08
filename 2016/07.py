def get_input(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def is_abba(s: str, i: int) -> bool:
    if any([ch in "[]" for ch in s[i : i + 4]]):
        return False
    a, b, c, d = [ch for ch in s[i : i + 4]]
    return (a != b) and (c != d) and (a == d) and (b == c)


def is_aba(s: str, i: int) -> bool:
    if any([ch in "[]" for ch in s[i : i + 3]]):
        return False
    a, b, c = [ch for ch in s[i : i + 3]]
    return (a != b) and (a == c)


def get_bab(s: str, i: int) -> str:
    a, b = [ch for ch in s[i : i + 2]]
    return "".join([b, a, b])


def solve(data: list[str]):
    tls = 0

    for s in data:
        n = len(s)

        hypernet_count = 0
        is_abba_in_hypernet = False
        is_abba_tls = False

        for i in range(n - 3):
            if s[i] == "[":
                hypernet_count += 1

            if s[i] == "]":
                hypernet_count -= 1

            if is_abba(s, i):
                if hypernet_count > 0:
                    is_abba_in_hypernet = True
                    break
                is_abba_tls = True

        if is_abba_tls and not is_abba_in_hypernet:
            tls += 1

    print(tls)


def example():
    fname = "input/2016/07E.txt"
    data = get_input(fname)
    solve(data)


def main():
    fname = "input/2016/07.txt"
    data = get_input(fname)
    solve(data)


example()
main()
