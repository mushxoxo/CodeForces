for _ in range(int(input())):
    n,l,r = map(int, input().split())
    lst = list(map(int, input().split()))
    print(min(sum(sorted(lst[l-1:])[:r-l+1]), sum(sorted(lst[:r])[:r-l+1])))

    
