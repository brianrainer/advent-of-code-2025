def is_nice(s: str) -> bool:
    vowel_set = set("aeiou")
    vowel = 0

    is_double = False
    
    naughty_dict = {
        "a": "b",
        "c": "d",
        "p": "q",
        "x": "y"
    }
    is_naughty = False

    for i, ch in enumerate(s):
        if ch in vowel_set:
            vowel += 1
        if i == 0:
            continue
        prev = s[i-1]
        if prev == ch:
            is_double = True
        if prev in naughty_dict and naughty_dict[prev] == ch:
            is_naughty = True
            break
    return vowel >= 3 and is_double and not is_naughty


def is_nice_new(s: str) -> bool:
    is_between = False
    has_two_pair = False

    for i in range(2, len(s)):
        if s[i-2] == s[i]:
            is_between = True
            break
    
    last_position = {
        s[0:2]: 1
    }

    for i in range(3, len(s)):
        s2 = s[i-2:i]
        if s2 in last_position:
            if last_position[s2] < i-2:
                has_two_pair = True
                break
        last_position[s2] = i-1
    return is_between and has_two_pair


with open("5A.txt", "r") as file:
    lines = file.readlines()

    ans = 0
    for line in lines:
        if is_nice_new(line):
            # print(line)
            ans += 1
    print(ans)