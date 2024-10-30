for _ in range(int(input())):
    n = int(input())
    data = [int(i) for i in input().split()]
    
    sorted_data = sorted(data)

    if data == sorted_data:
        print("Yes")
        continue

    all_possible_cases = sorted_data + sorted_data

    for j in range(n):
        if all_possible_cases[j:j+n] == data:
            print("Yes")
            break
    else:
        print("No")