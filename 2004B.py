for _ in range(int(input())):
    l, r = map(int, input().split())
    L, R = map(int, input().split())

    print(max(1, min(r, R) - max(l, L) + (l != L) + (r != R)))