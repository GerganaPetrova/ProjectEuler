from math import sqrt

def d(n):
    s = 1
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            s += i + n / i
    return s

result = 0
for i in range(2,10000):
    a = d(i)
    if a > i and d(a) == i:
        result += a + i

 
