set = set(i**2 for i in range(1,100,2))

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    count = 0
    sum = 0

    for i in lst:
        sum+=i
        if sum in set:
            count+=1
    print(count)
