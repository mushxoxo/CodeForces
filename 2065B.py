for _ in range(int(input())):
    word = input()
    word = [i for i in word]

    if len(word) == 1:
        print(1)
    else:
        pos = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                print(1)
                break
        else:
            print(len(word))
