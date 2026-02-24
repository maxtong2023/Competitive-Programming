rook = input()
knight = input()

# Fixed mapping (corrected 'e')
mapping = {
    "a": 1, "b": 2, "c": 3, "d": 4, 
    "e": 5, "f": 6, "g": 7, "h": 8,
}

r_col, r_row = mapping[rook[0]], int(rook[1])
k_col, k_row = mapping[knight[0]], int(knight[1])

forbidden = set()

for i in range(1, 9):
    forbidden.add((r_col, i))
    forbidden.add((i, r_row))
#knight
forbidden.add((k_col, k_row))

offsets = [
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
]


for dc, dr in offsets:
    nc, nr = k_col + dc, k_row + dr
    if 1 <= nc <= 8 and 1 <= nr <= 8:
        forbidden.add((nc, nr))

for dc, dr in offsets:
    nc, nr = r_col + dc, r_row + dr
    if 1 <= nc <= 8 and 1 <= nr <= 8:
        forbidden.add((nc, nr))

print(64 - len(forbidden))