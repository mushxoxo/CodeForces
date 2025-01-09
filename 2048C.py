for _ in range(int(input())):
    s = input()
    n = len(s)
    k = s.find('0')
    if k == -1:
        print(1, 1, 1, n)
    else:
        l = n - k
        p = s[k:].find('1')
        if p == -1:
            k = 0
        else:
            k = max(k - p, 0)
        print(k + 1, k + l, 1, n)