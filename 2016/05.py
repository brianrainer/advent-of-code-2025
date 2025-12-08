import hashlib


def get_md5_hash(s: str) -> str:
    md5_hash_object = hashlib.md5(s.encode("utf-8"))
    hex_digest = md5_hash_object.hexdigest()
    return hex_digest


def solve(seed):
    old_password = ""
    password = ["x" for _ in range(8)]
    i = 0
    x_count = 8
    while x_count:
        encrypted = get_md5_hash(seed + str(i))
        if encrypted[:5] == "00000":
            if len(old_password) < 8:
                old_password += encrypted[5]
            print(i, encrypted)
            pos = int(encrypted[5]) if "0" <= encrypted[5] <= "7" else 8
            if pos != 8 and password[pos] == "x":
                password[pos] = encrypted[6]
                x_count -= 1
        i += 1
    print("PART 1:", old_password)
    print("PART 2:", "".join(password))


example_seed = "abc"
seed = "uqwqemis"

solve(example_seed)
solve(seed)
