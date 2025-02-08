for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int,input().split()))
    s = 0
    for x,y in zip(a,a[1:]):
        if x==y:
            a.remove(x)
            a.remove(x)
            s=x
            break
    
    for x,y in zip(a,a[1:]):
        if s+s+x>y:
            print(s,s,x,y)
            break
    else:
        print(-1)






