def same_digits(n):
    s1 = sorted(str(n))
    s2 = sorted(str(n * 2))
    s3 = sorted(str(n * 3))
    s4 = sorted(str(n * 4))
    s5 = sorted(str(n * 5))
    s6 = sorted(str(n * 6))
    if s1 == s2 == s3 == s4 == s5 == s6:
        return True
    return False

def permuted_multiples():
    n = 1 
    while not same_digits(n):
        n += 1
    return n    
