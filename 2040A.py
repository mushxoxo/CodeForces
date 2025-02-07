for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    r = [i%k for i in a]
 
    for i in set(r):
        if r.count(i) == 1:
            print('yes')
            print(r.index(i)+1)
            break
    else: print('no')
