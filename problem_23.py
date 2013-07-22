import math

def sum_of_divisors(n):
    s = 1 
    sq = math.sqrt(n)
    for i in range(2, int(sq) + 1):
        if n % i == 0:
            s += i + n / i
    if sq == int(sq):
        s -= sq
    return s

def sum_of_abundant_numbers():
    abundant_numbers = set() 
    result = 0
    for i in range(20161):
        if sum_of_divisors(i) > i:
            abundant_numbers.add(i)
        if not any((i - a in abundant_numbers) for a in abundant_numbers):
           result += i 
    return result


