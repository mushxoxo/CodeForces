for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    for i,val in enumerate(lst, start=1):
        # print(i,val)
        if val<=2*(n-i) or val<=2*(i-1):
            print("NO")
            break

    else:
        print("YES")


