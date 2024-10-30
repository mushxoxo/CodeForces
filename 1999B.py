for _ in range(int(input())):

    a,b,c,d = map(int, input().split())
    win = 0

    if (a>=c and b>d) or (a>c and b>=d):
        win+=2
    if (a>=d and b>c) or (a>d and b>=c):
        win+=2
    print(win) 