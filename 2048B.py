for _ in range(int(input())):
    n,k = map(int, input().split())

    i,j = 1,n

    lst = []

    for x in range(n):
        if((x+1)%k == 0):
            lst.append(i)
            i+=1
        else:
            lst.append(j)
            j-=1

    print(*lst)