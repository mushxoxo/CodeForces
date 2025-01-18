for _ in range(int(input())):
    s = input()[::-1]

    for i in s:
        if i == "q":
            print("p", end = "")
        elif i == "p":
            print("q", end="")
        else:
            print("w", end = "")

    print()
