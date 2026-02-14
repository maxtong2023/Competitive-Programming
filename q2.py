n = list(input().split())

# what does it mean to be a permutation?

# the skyline will always have at least 1, 1. It will always be at least 1, 2, or 2, 1
nums = []

total = n[0]
left = n[1]
right = n[2]



def solve(n):
    if n[1] + n[2] > n[0] or n[1] + n[2] < 3:
        print("no")
        return 
    
    # increment from total - right, right times
    # 
    count = 0
    for i in range(right):
        if i != right - 1: 
            nums.append(total - right + count)
            count +=1
        else: 
            nums.append(total) # append largest
    
    # do the middle stuff

    remainder = total - right - left

    for i in remainder: 
        nums.append(i + 1)

    # decrement from the end. Make sure it starts with the second largest
    second = total - 1
    count = 0
    for i in left: 
        nums.append(second - count)
        count +=1 
    
    print(nums)

ans = solve(n)




    
    
    

    
    
    
