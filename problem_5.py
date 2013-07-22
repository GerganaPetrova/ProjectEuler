def findPrime(n):
    for x in range(2, n+1):
        if float(n) % x == 0:
            return x

res = 1
for x in range(1, 21):
    if res % x != 0:
        n = findPrime(x)
        res *= n

print(res)
