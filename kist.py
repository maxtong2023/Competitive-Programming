#manhattan distance

n, k = map(int, input().split())

instructions = input()

grid = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(".")
    grid.append(temp)

# center

row = n // 2
col = n // 2

for instruction in instructions: 
    if instruction == "U":
        if row - 1 >= 0:
            row -= 1
    elif instruction == "D":
        if row + 1 < n:
            row += 1
    elif instruction == "L":
        if col - 1 >= 0:
            col -= 1
    elif instruction == "R":
        if col + 1 < n:
            col += 1
    else:
        for i in range(n):
            for j in range(n):
                distance = abs(row - i) + abs(col - j)
                if distance < k:
                    grid[i][j] = instruction

for row in grid:
    print("".join(row))
