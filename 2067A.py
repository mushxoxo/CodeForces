for _ in range(int(input())):
    x, y = map(int, input().split())

    if y == x + 1 or ((x-y+1) % 9 == 0 and x-y+1>=9):
        print("Yes")
    else:
        print("No")