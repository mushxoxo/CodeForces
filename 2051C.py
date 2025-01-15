for _ in range(int(input())):
    n, m, k = map(int, input().split())
    set_m = set(map(int, input().split()))
    set_k = set(map(int, input().split()))

    if k<n-1:
        print("0"*m, end='')
    elif k == n:
        print("1"*m, end='')
    else:
        for i in set_m:
            if i in set_k:
                print("0", end='')
            else:
                print("1", end='')
    
    print()
