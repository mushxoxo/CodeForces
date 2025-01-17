for _ in range(int(input())):
    n = int(input())

    pair = 0

    for i in range(n):
        for j in range(n):
            if i+j == n:
                pair+=1

    print(pair)