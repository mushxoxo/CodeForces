for _ in range(int(input())):
    n, a ,b = map(int, input().split())

    print(["No","Yes"][(a-b)%2==0])