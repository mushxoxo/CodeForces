for _ in range(int(input())):
    n,k = map(int,input().split())
    a = sorted(map(int,input().split()))
    x = 0
    # print(a)
    while a and a[-1] + x <= k:
        x += a.pop()
    print(k-x)