
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = sum(lst)
    while n>1:
        n-=1
        lst = [lst[i + 1] - lst[i] for i in range(n)]
        ans = max(ans, abs(sum(lst)))

    print(ans)






