N = int(input())
arr = list(map(int, input().split()))

total = 0
result = []


for i in range(len(arr)):
    right = len(arr) - i - 1
    left = i

    if right % 2 == 0: 
        # right is even
        # look at the left side of the array
        for k in range(i, 0, -2):
            index = k -1
            result.append(arr[index] + arr[i])

    elif left % 2 == 0:
        # left is even
        for k in range(i, len(arr), 2):
            index = k + 1 # basically 2k + 1    
            result.append(arr[index] + arr[i])

total = max(result)
print(total)
            
            
            
    


