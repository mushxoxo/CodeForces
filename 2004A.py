for _ in range(int(input())):
    t = int(input())
    x = list(map(int, input().split()))
    if len(x) == 2 and x[1]-x[0]!=1:
        print("YES")
    else:
        print("NO")