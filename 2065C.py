for _ in range(int(input())):

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    a[0] = min(a[0], b - a[0])
 
    for i in range(1, n):
        t = b - a[i], a[i]
 
        if min(t) >= a[i - 1]:
            a[i] = min(t)
        elif max(t) >= a[i - 1]:
            a[i] = max(t)
        else:
            print("NO")
            break
    else:
        print("YES")