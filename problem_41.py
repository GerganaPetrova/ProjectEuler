def is_pandigital(string,n):
    if len(string) > n:
        return False
    digits = list(string)
    check = []
    for i in range(1,n+1):
        check.append(str(i))

    if sorted(digits) == check:
        return True
    return False

def is_prime(n):
    if n < 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
       if n % x == 0:
            return False
    return True 

def pandigital_prime():
    number = 7654321
    while not(is_prime(number) and is_pandigital(str(number), 7)):
        number -= 1
    return number    
