for _ in range(int(input())):
    n,k = map(int, input().split())
    a = input().split()
    a = [int(i) for i in a]
    a.sort(reverse= True)
    a.pop(0)
    count = 0
    for i in a:
        if i == 1:
            count+=1
        else:
            count+=2*i-1
    print(count)