t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for k in range(n):
        for j in range(k + 1, n):
            temp = arr[k] ^ arr[j]
            if temp > result:
                result = temp
    print(result)
