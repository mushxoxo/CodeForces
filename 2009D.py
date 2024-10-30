from itertools import combinations

for _ in range(int(input())):
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))
    
    subset = list(combinations(arr, 3))

    print(subset[1][1][1])

    for i in range(len(subset)):
        for j in range(3):
            for k in range(2):

                x = 
