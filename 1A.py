with open("1A.txt", "r") as file:
    lines = file.readlines()
    
    ans = 0
    current = 50
    for line in lines:
        direction = line[0]
        turn = int(line[1:])
        
        if direction == 'L':
            current -= turn
        else:
            current += turn
        
        current %= 100
        if current == 0:
            ans += 1
    
    print(ans)
