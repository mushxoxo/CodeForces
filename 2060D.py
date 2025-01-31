for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))


    if n == 1:
        print("YES")
    
    elif lst[0]>lst[1]:
        print("NO")
    
    else:
        for i in range(n-2):
            
            if lst[i+1] - lst[i] > lst[i+2]:
                print("NO")
                break
            else:
                lst[i+1] -= lst[i]
                lst[i] = 0

        else:
            print("YES")



