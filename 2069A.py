for _ in range (int(input())):
    n = int(input())
    lst = "".join(map(str, input().split()))
    #print(lst)

    for i in range(n):
        if lst[i:i+3] == '101':
            print("NO")
            break
    else:
        print("YES")

