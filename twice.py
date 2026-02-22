n = int(input())
testcases = []
for i in range(n):
    test = []
    test.append(int(input()))
    test.append(list(map(int, input().split())))
    testcases.append(test)

#result = []
for case in testcases: 
    score = 0

    freqs = {}

    length = case[0]
    arr = case[1]

    for num in arr: 
        freqs[num] = freqs.get(num, 0) + 1
    for freq in freqs: 
        # order does not matter?
        pairs = freqs[freq] // 2 # floor division
        score += pairs

    print(score)
#print(result)