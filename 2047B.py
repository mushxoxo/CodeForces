for _ in range(int(input())):
    dic = {}

    n = int(input())

    str = input()
    lst = list(str)

    for char in lst:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    max_char = None
    min_char = None


    dic = list(sorted(dic.items(), key= lambda x: x[1]))

    min_char = dic[0][0]
    max_char = dic[-1][0]

    str = str.replace(min_char, max_char, 1)

    print(str)

