t = int(input())

arrayLengths = []
arrays = []

for i in range(t):
    arrayLengths.append(int(input()))
    arrays.append(list(map(int, input().split())))

# need the duplicates of the largest number, not duplicates of any number. oops. 
for i in range(t):
    for k in range(arrayLengths[i]):
        freqs = {}
        count = 1
        top = max(arrays[i])

        for j in arrays[i]:
            freqs[j] = freqs.get(j, 0) + 1
            if freqs[j] > 1 and j == top:
                count +=1
    print(count)
