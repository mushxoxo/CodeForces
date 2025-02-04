for _ in range(int(input())):
    n = int(input())

    coins = 1

    while n > 3:
        n //= 4
        coins*=2

    print(coins)
