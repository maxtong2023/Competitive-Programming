t = int(input())

def solve(t: int) -> int:
    if t <= 360:
        return 0
    if t <= 390:
        return t - 360  
    if t <= 540:
        return 30
    if t <= 585:
        return max(t - 540, 30)
    if t <= 600:
        return 45
    return max(t - 600, 45)

print(solve(t))