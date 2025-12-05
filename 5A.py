def is_overlap(p: tuple[int,int], q: tuple[int,int]) -> bool:
    i, j = p
    x, y = q
    return (i <= x <= j) or (i <= y <= j) or (x <= i <= y) or (x <= j <= y)

def process_data(data: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_data = []
    data.sort()

    new_data.append(data[0])
    for i in range(1, len(data)):
        x, y = data[i]
        if is_overlap(new_data[-1], data[i]):
            pi, pj = new_data.pop()
            # print(pi, pj, x, y)
            x, y = min(x, pi), max(y, pj)
            # print(x, y)
        new_data.append((x,y))

    return new_data

with open("5A.txt", "r") as file:
    lines = file.readlines()

    ans = 0
    data = []
    is_query = False
    for line in lines:
        if line == "\n":
            is_query = True
            data.sort()
            continue
        if not is_query:
            start, end = [int(x) for x in line.split('-')]
            data.append((start,end))
            continue
        # process query
        q = int(line)
        for (start, end) in data:
            if q >= start and q <= end:
                ans += 1
                break
    
    print(ans)
    new_data = process_data(data)

    # print(new_data)
    count = 0
    for (start, end) in new_data:
        count += end - start + 1
    print(count)