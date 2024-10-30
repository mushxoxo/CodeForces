for _ in range(int(input())):
    I = input
    n,m=map(int,I().split())
    a=' '.join(I()for _ in[0]*n).split()
    print(*(a[1:]+a[:1],[-1])[n+m<3])