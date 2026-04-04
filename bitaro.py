n, m = map(int, input().split())

links = []
for i in range(m):
    links.append(list(map(int, input().split())))


# n < 1000
# m = n -1 
# there exists a permutation P of (1, 2, ..., n) such that for each i 1, 2, ... N - 1 there is a road between Pi and Pi+1 

# basically it just says that the links are a straight line.

