from math import factorial

def c(n,r):
    return  factorial(n) / (factorial(r) * factorial(n - r))

def combinatoric_selections():
    res = []
    for n in range(1,101):
        for r in range(0,101):
            if r <= n:
                s = c(n,r)
                if s > 1000000:
                    res.append(s)
    return len(res)
