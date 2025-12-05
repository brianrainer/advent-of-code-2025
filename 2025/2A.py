def is_valid_2(num):
    s = str(num)
    n = len(s)
    if n & 1 == 1:
        return False
    return s[:n//2] == s[n//2:]

def is_valid_k(num, div_k):
    s = str(num)
    n = len(s)
    if n % div_k != 0:
        return False
    split_s = list(map("".join, zip(*[iter(s)]*div_k)))
    return len(set(split_s)) == 1

with open("2A.txt", "r") as file:
    lines = file.readline().split(',')
    ans = 0
    for line in lines:
        start, end = [int(x) for x in line.split('-')]
        for x in range(start, end+1):
            is_found = any([is_valid_k(x,k) for k in range(1, len(str(x)) // 2 + 1)])
            if is_found:
                ans += x
    print(ans)
