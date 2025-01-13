for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    if any((lst[i+1]>(lst[i]/2) and (lst[i+1] < 2*(lst[i]))) or (lst[i]>(lst[i+1]/2) and (lst[i] < 2*(lst[i+1]))) for i in range(n-1)):
        print("Yes")
    else:
        print("No")