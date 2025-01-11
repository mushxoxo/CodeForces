for _ in range(int(input())):
    n, a, b,c = map(int, input().split())
    lst = [a, b, c]
    approx = n//(a+b+c)

    sum = approx*(a+b+c)
    count = 0
    x=0

    while sum<n:
        sum+=lst[x]
        count+=1
        x+=1

    print(3*approx+count)