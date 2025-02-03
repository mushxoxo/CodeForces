for _ in range(int(input())):

    lst = []
    n,m = map(int, input().split())

    x = m
    y = m

    for i in range(n):
        a,b = tuple(map(int, input().split()))
        x += a
        y += b
        lst.append((a,b))

    # print(lst)

    x -= lst[0][0]
    y -= lst[0][1]

    

    print(2*(x+y))


