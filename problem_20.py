from math import factorial

def factorial_digit_sum():
    return sum(map(int, list(str(factorial(100)))))
