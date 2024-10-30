for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a, key=a.count)

    print(len(a)-a.count(m))