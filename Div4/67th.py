t = int(input())

n = []
for i in range(t): 
    n.append(int(input()))


for i in range(t):
    print(min(n[i] + 1, 67))