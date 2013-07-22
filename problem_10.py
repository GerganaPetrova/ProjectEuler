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

def sum_primes():
    gen = gen_primes()
    s = gen.next()
    my_sum = 0 
    while s <= 2000000:
        my_sum += s
        s = gen.next()
    return my_sum 
     
print sum_primes()        
