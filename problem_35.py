import itertools,math

def numbers_from_digits(n):
    digits = list(str(n))
    numlist = [''.join(n) for n in list(itertools.permutations(digits))]
    return [int(num) for num in numlist]

def is_prime(n):
    if n < 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
       if n % x == 0:
            return False
    return True 

def permutations_is_prime(n):
    perm = numbers_from_digits(n)
    return all(is_prime(elem) for elem in perm)

def circular_primes():
    result = []
    for i in range(1000000):
        if is_prime(i) and permutations_is_prime(i):
            result.append(i)
    return len(result)           
