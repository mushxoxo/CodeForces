
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
 
    max_num = max(arr)
 
    for i in range(m):
        opp , start, end = input().split() 
        
        if int(start) <= max_num <= int(end):
            if opp == "+": 
                max_num+=1
            else:
                max_num-=1
        print(max_num)
 
