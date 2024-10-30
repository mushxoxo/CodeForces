for _ in range(int(input())):
    n = int(input())
    arr = []

    for i in range(n):
        arr.append(input())

    for i in range(n-1, -1, -1):
        for j in range(4):
            if arr[i][j] == '#':
                print(j + 1, end=" ")
    print()
