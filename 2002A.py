for _ in range(int(input())):
    n,m,k = map(int, input().split())
    col = 0
    
    if n<=k and m<=k:
        col = n*m
    elif n<=k or m<=k:
        col = k*(min(n,m))
    else:
        col = k*k
    print(col)