for _ in range(int(input())):
    n = int(input())
    s = input()
    s = [int(i) for i in s]
    ans = 0

    unique = set(s)

    if unique == {1}:  # All elements are 1
        ans = 1
    elif unique == {0}:  # All elements are 0
        ans = 0
    else:
        f = int(0) # Track previous value
        for num in s:
            if num != f:  # Count distinct contiguous segments
                ans += 1
                f = num

    print(ans)






