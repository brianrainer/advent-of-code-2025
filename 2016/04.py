def get_input(filename: str) -> list[list[str]]:
    with open(filename, "r") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            s = line.rstrip("]\n").split("[")
            data.append([x for x in s[0].split("-")] + [s[-1]])
    return data


def count_char(data: list[str]) -> dict[str, int]:
    ch_map = {}
    for s in data:
        for ch in s:
            if ch not in ch_map:
                ch_map[ch] = 0
            ch_map[ch] += 1
    return ch_map


def decrypt_message(s: str, shift: int) -> str:
    message = ""
    for ch in s:
        if ch == "-":
            message += " "
            continue
        num = (ord(ch) - ord("a")) + shift
        num %= 26
        message += chr(num + ord("a"))
    return message


def solve(data: list[list[str]]):
    ans = 0
    is_found = False
    for s in data:
        ch_map = count_char(s[:-2])

        top_5 = sorted(ch_map.items(), key=lambda d: (-d[1], d[0]))[:5]
        checksum = "".join([x[0] for x in top_5])

        if checksum != s[-1]:
            continue

        shift_id = int(s[-2])
        ans += shift_id

        if is_found:
            continue
        encrypted = "-".join(s[:-2])
        decrypted = decrypt_message(encrypted, shift_id)
        if "north" in decrypted:
            print("PART 2:", shift_id, decrypted)
            is_found = True

    print("PART 1:", ans)


def example():
    data = get_input("input/2016/04E.txt")
    solve(data)


def main():
    data = get_input("input/2016/04.txt")
    solve(data)


example()
main()
