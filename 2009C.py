import math

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    
    direction = 0
    moves = 0

    if x >= y:
        moves = math.ceil(y/k)*2

        temp = x-(k*math.ceil(y/k))

        if temp > x:
            moves = moves

        else:
            moves += math.ceil(x/k)*2 - 1


    else:

        moves = math.ceil(x/k)*2

        temp = y-(k*math.ceil(x/k))


        if temp > x:
            moves = moves

        else:
            moves += math.ceil(x/k)*2
    print(moves)
    

