
import math

for _ in range(int(input())):
	n = int(input())
	lst = [int(x) for x in input().split()]
	u = list(set(lst))
	for i in range(len(u)):
		u[i] = lst.count(u[i])
	u.sort()
	print(2*(math.ceil(u.count(1)/2))+len(u)-u.count(1))