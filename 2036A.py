for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    print( "Yes" if all( abs(lst[i]-lst[i+1])  in [5,7] for i in range(n-1)) else "No" )
