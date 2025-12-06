def calculate_area(wraps: list[int]) -> int:
    wraps.sort()
    h, w, l = wraps[0], wraps[1], wraps[2]  # noqa: E741
    return 3 * h * w + 2 * w * l + 2 * h * l


def calculate_ribbon(wraps: list[int]) -> int:
    wraps.sort()
    h, w, l = wraps[0], wraps[1], wraps[2]  # noqa: E741
    return 2 * h + 2 * w + h * w * l


with open("2A.txt", "r") as file:
    lines = file.readlines()

    ans = 0
    for line in lines:
        wraps = [int(x) for x in line.strip().split("x")]
        ans += calculate_ribbon(wraps)
    print(ans)
