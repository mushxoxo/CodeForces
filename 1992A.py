for _ in range(int(input())):
    data = input().split()
    data = [eval(_) for _ in data]
    for i in range(5):
        data[data.index(min(data))] = min(data)+1
    print(data[0]*data[1]*data[2])

