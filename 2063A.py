for _ in range(int(input())):
    l,r = map(int, input().split())

    if l==1 and r==1:
        print(1)
    else:
        print(r-l)