n = int(input())
s = input()

def solve(n, s):
    stack = []
    for char in s:
        if char == "J":
            if stack and type(stack[-1]) == int: 
                stack[-1] += 1
            else:
                stack.append(1)
        elif char == "O":
            stack.append("O")
        elif char == "I":
            if len(stack) >=2 and stack[-1] == "O" and type(stack[-2]) == int:
                # found a JOI chunk, replace with the pattern that we found. 
                stack.pop()
                numj = stack.pop()

                stack.append("O")
                stack.append("I")
                stack.append(numj)

            else:
                stack.append("I")
    result = []

    for i in stack: 
        if type(i) == int:
            result.extend(["J"] * i)
        else:
            result.append(i)

    return "".join(result)

print(solve(n, s))

