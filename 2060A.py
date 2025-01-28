# for _ in range(int(input())):
#     a,b,d,e = map(int, input().split())
#     fib1 = 0
#     fib2 = 0

#     lst1 = [a,b,a+b,d,e]
#     lst2 = [a,b,e-d,d,e]

#     for i in range(3):
#         if lst1[i+2] == lst1[i]+lst1[i+1]:
#             fib1+=1
#         if lst2[i+2] == lst2[i]+lst2[i+1]:
#             fib2+=1

#     print(max(fib1,fib2))


for i in range(int(input())):
    x,y,z,w=map(int,input().split())
    count={x+y,z-y,w-z}
    print(count)
    print(4-len(count))