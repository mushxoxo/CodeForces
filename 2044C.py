for i in range(int(input())):
    m,a,b,c = map(int,input().split())
    
    print(min(2*m,min(m,a)+min(m,b)+c))