t = int(input())

arrayLengths = []
arrays = []

for i in range(t):
    arrayLengths.append(int(input()))
    arrays.append(list(map(int, input().split())))

for i in range(t):
    if sorted(arrays[i]) == arrays[i]:
        print(arrayLengths[i])
    else:
        print(1)

