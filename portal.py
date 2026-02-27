t = int(input())

nxy = []
permutation = []

for i in range(t):
    nxy.append(list(map(int, input().split())))
    permutation.append(list(map(int, input().split())))

# can we try to define the constraint?

# the numbers in the middle portion, between the two portals have to be the same, but like they do 
# in the first test case, you can shift it as much as you want. So always try to get the smallest possible
# lexo whatever permutation in the middle portion.

for i in range(t):
    n = nxy[i][0]
    x = nxy[i][1]
    y = nxy[i][2]
    left = permutation[i][:x]
    right = permutation[i][y:]
    middle = permutation[i][x:y]

    # get thebest permutation for the middle portion first cuz that can be shifted as much as we want

    best = middle

    for k in range(len(middle)):
        temp = middle[k:] + middle[:k]
        if temp < best:
            best = temp

    # 

    inserted = False
    answer = []

    for i in (left +right ):
        if not inserted and (best + [i] < [i] + best): 
            inserted = True
            answer.extend(best)
        
        answer.append(i)

    if not inserted: 
        answer.extend(best)
    print(*answer)
