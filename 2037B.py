for _ in range(int(input())):
   k = int(input())
   a = [int(i) for i in input().split()]
   for i in range(1, k-1):
      if((k - 2) % i == 0 and (k-2)/i in a and i in a):
         print(int((k-2)/i), i)
         break

