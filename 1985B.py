for _ in range(int(input())):
    max_sum = 0
    opt = 2
    n = int(input())
    for i in range(2,n+1):
        k = n // i
        sum = i * (k * (k+1))//2
        if sum > max_sum:
            max_sum = sum
            opt = i
    print(opt)