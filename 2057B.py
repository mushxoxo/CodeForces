from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = Counter(input().split())
    m = len(lst)


    for i in sorted(lst.values()):
        if k<i:
            break
        k-=i
        m-=1

    print(max(1,m))

