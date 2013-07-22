import math

def triangle_number(n):
    return (n * (n + 1)) / 2

def count(n):
    c = 0
    isq = int(math.sqrt(n))
    if math.sqrt(n) == isq:
        c += 1

    for i in range(1, isq -1):
        if n % i == 0:
            c += 2
    return c

def func():
    n = 0
    t = triangle_number(n)
    m = count(t)
    while m < 500:
        n += 1
        t = triangle_number(n)
        m = count(t)
    return t

print func()        
