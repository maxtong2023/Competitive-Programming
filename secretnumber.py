t = int(input())
cases = []
for i in range(t):
    cases.append(int(input()))


# two constraints

# n = x + y 
# y must be made by adding zeroes to x.  * 10^z

# number of digits of x will always be at least 1 less than the number of digits of n 

# n = x + y
# 1. x = n - y

# 2. x * 10^z = y

# given n, three unknowns, iterate z? z is greater than 1 and less than digits n.

# two equations two unknowns, should be able to solve for x and y. ???

# 3. x + (x * 10^z) = n
# 4. x(1 + 10^z) = n
# 5. x = n/(1 + 10^z)


for num in cases: 
    result = []
    count = 0 
    cap = len(str(num)) # upper bound for z

    for z in range(1, cap, 1):
        x = num // (1 + pow(10, z))
        y = x * (pow(10, z))

        if x + y == num: 
            result.append(x)
            count +=1 
    
    print(count)
    if len(result) > 0: 
        result.sort()
        print(*result)
    








