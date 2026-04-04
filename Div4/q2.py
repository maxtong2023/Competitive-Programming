# must negate 6 numbers. Instead of thinking about the numbers you negate, think about the numbers you don't negate. 

t = int(input())

arr = []
for i in range(t):
    arr.append(list(map(int, input().split())))


# i think you want to NOT negate the largest of 7 numbers, and negate the rest.


for i in range(t): 
    total = 0
    largest = max(arr[i])

    for j in range(7):
        total -= arr[i][j]
    
    total += largest
    total += largest
    print(total)

