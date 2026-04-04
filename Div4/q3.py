# basically, you are given an integer n, and you have to generate a permutation of 3n length.
from collections import deque

t = int(input())

n = []
for i in range(t): 
    n.append(int(input()))


# the length of the partition is 3. ALWAYS ODD! Largest element is in the middle.

for i in range(t): # i think the pattern needs to be lowest, largest, largest - 1
    nums = list( range(1, 3 * n[i] + 1))
    nums = deque(nums)
    result = []
    
    for k in range(n[i]):
        result.append(nums.popleft())
        result.append(nums.pop())
        result.append(nums.pop())
    print(*result)


