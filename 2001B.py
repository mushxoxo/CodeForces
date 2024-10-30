for _ in range(int(input())):
    n = int(input())
    s = n
    e = int(2)
    
    if n%2==0:
        print(int(-1))
    else:

        for i in range(n):
            if i<(n-1)/2:
                print(s ,end = " ")
                s-=2
            elif i == (n-1)/2:
                print(int(1), end = " ")
            else:
                print(e, end=" ")
                e+=2
        print("")
