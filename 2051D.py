import bisect

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    lst = sorted(list(map(int, input().split())))

    total = sum(lst)
    count = 0
    
    
    for i in range(n):
        left = bisect.bisect_left(lst, total-y-lst[i], i+1)
        right = bisect.bisect_right(lst, total-x-lst[i], i+1)

        count+=right-left

    print(count)

            



