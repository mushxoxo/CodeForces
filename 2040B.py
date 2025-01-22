import math

for _ in range(int(input())):
    n = int(input())
    
    ans = 1
    cur = 1

    while cur<n:
        ans+=1
        cur = 2*(cur+1)

    print(ans)

