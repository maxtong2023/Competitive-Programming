t = int(input())

n = []
for i in range(t):
    n.append(int(input()))

result = []


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def findPrimes(count):
    res = []
    x = 2
    while len(res) < count:
        if isPrime(x):
            res.append(x)
        x += 1
    return res


primes = findPrimes(max(n) + 1)

for i in range(t):
    result = []
    for k in range(n[i]):
        num = primes[k] * primes[k + 1]
        result.append(num)
    print(*result)
