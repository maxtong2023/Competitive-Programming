n = int(input())

confidence = []
for i in range(n):
    confidence.append(list(map(int, input().split())))

count = 0

for i in confidence: 
    score = 0
    for k in i: 
        if k == 1: 
            score += 1
            if score >= 2: 
                count +=1 
                break
print(count)
