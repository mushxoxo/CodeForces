for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if any(a.count(i)%2!=0 for i in set(a)):
        print("Yes")
    else:
        print("No")
