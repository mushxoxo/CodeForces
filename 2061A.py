for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1

    if even > 0:
        print(1+odd)
    else:
        print(odd - 1)