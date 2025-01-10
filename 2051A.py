for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum = 0
    for x,y in zip(a[:n-1], b[1:]):
        if x>y:
            sum+= (x-y)

    print(sum+a[-1])