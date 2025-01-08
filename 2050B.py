for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sum1 = 0
    sum2 = 0
    count1 = 0
    count2 = 0
    for i in range(0,n,2):
        sum1+=lst[i]
        count1+=1
    for i in range(1,n,2):
        sum2 += lst[i]
        count2 += 1

    # print(sum1,count1, sum2, count2

    if sum1%count1 == 0 and sum2%count2==0 and sum1/count1 == sum2/count2:
        print("YES")
    else:
        print("No")
    
