for _ in range(int(input())):
    alp = input()
    list = alp.split()

    list.replace(list[0][0], list[1][0])
    print(list)