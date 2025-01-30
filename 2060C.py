for _ in range(int(input())):
    n, k = map(int, input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    score=0
    start,end=0,n-1
    while start<end:
        if lst[start]+lst[end]==k:
            score+=1
            start+=1
            end-=1
        elif lst[start]+lst[end]<k:
            start+=1
        else:
            end-=1
    print(score)