for _ in range(int(input())):
    n = int(input())

    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    if len(set(lst1)) + len(set(lst2)) > 3:
        print("YES")
    else:
        print("NO")