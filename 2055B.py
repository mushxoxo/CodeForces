for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(n):
        if b[i] > a[i]:
            req = b[i] - a[i] 
            for j in range(n):
                if i != j:
                    if a[j] - b[j] < req:
                        print("NO")
                        break
            else:
                continue 
            break
    else:
       
        print("YES")


                    



                        