for _ in range(int(input())):
    n = int(input())
    data = [int(x) for x in input().split()]
    ans = 1e9
    for i in range(n-1):
        ans = min(ans, max(data[i], data[i+1]))

    print(int(ans)-1)