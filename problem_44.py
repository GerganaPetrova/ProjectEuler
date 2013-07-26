def nth_pentagon_number(n):
    return n * (3*n - 1) / 2

def smallest_pair():
    i = 0
    pn = set()
    while True:
        i += 1
        p = nth_pentagon_number(i)
        pn.add(p)
        for n in pn:
            if p - n in pn and p - 2*n in pn:
                return p - 2*n

    
