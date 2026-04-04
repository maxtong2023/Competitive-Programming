n, m, k = map(int, input().split()) 

alive = []
for i in range(m + 1):
    alive.append(1)

bombs = []
for i in range(k):
    bombs.append(list(map(int, input().split()))) 

for bomb in bombs:

    col = bomb[0]
    row = bomb[1]
    time = bomb[2]

    for i in range(1, m + 1):
        if time >= i: 
            z = time - i + 1
            
            if z <= n:
                if abs(col - z) <= row:
                    alive[i] = 0
survivors = 0
for i in range(1, m + 1):
    if alive[i] == 1:
        survivors += 1
print(survivors)
