def gen_primes():
    d = {}  
    q = 2  
    while True:
        if q not in d: 
            yield q        
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1

def nth_prime(n):
    return (j for i,j in enumerate(gen_primes()) if i == n-1).next()

print nth_prime(10001)    
