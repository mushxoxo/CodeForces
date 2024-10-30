def max_draws(case):
    result = []

    p1, p2, p3 = int(case[0]), int(case[1]), int(case[2])
    if (p1+p2+p3)%2 != 0:            
        result.append(-1)
    elif p1 + p2 <= p3:
        result.append(p1+p2)
    else:
        if p1 > (p3-p2):
            result.append((p1 + p2 + p3)//2)
        else:
            result.append(p1 + p2)
    return int(result[0])

n = int(input())

for i in range(0,n):
    case = input().split()
    print(max_draws(case))