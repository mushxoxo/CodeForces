for _ in range(int(input())):
    n,m = map(int, input().split())

    dic = {}

    for i in range(1,n+1):
        dic[i] = sum(list(map(int, input().split())))


    if n == 1:
        print(1)
    else:

        for key,val in dic.items():
            if val%m!=0:
                print(-1)
                break
        else:
            lst = sorted(dic, key = lambda x: dic[x])
            print(*lst)

