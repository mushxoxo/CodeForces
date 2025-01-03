for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().strip('0 ').split()))

    if 0 in lst:
        print(2)
    elif lst:
        print(1)
    else:
        print(0)