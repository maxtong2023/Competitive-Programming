N = int(input())

row = list(map(int, input().split()))
col = list(map(int, input().split()))

# create nxn grid 

grid = [[0 for i in range(N)] for j in range(N)]

# create the initial grid
for i in range(N):
    grid[0][i] = row[i]
    grid[i][0] = col[i]

# iterate through the grid and fill in the values: 

for i in range(1, N):

    for k in range(1, N):
        grid[i][k] = max(grid[i-1][k], grid[i][k-1])


# find number with the most occurences

freqs = {}

for i in range(N ):
    for k in range(N):
        if grid[i][k] in freqs:
            freqs[grid[i][k]] += 1
        else:
            freqs[grid[i][k]] = 1

max_num = max(freqs.keys())
max_freq_num = freqs[max_num]

print(max_num, max_freq_num)


