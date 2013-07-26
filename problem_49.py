def is_prime(n):
    if n < 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
       if n % x == 0:
            return False
    return True 

def is_perm(n1, n2):
    number1 = str(n1)
    number2 = str(n2)
    if sorted(number1) == sorted(number2):
       return True
    return False

def prime_permutations():
    n = 1489
    while True:
        a = n + 3330
        b = a + 3330
        if is_prime(n) and is_prime(a) and is_prime(b) and is_perm(n, a) and is_perm(n, b):
            break
        n += 2
    return str(n) + str(a) + str(b)         
