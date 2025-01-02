for _ in range(int(input())):
    n,m = map(int, input().split())
    length = 0
    count = 0
    lst = []

    for i in range(n):
        lst.append(input())

    for i in lst:
        if length+len(i) <= m:
            length+=len(i)
            count+=1
        else:
            break

    print(count)