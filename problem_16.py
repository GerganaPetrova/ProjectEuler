x = 2
n = 1000

def power_digit_sum(x,n):
    return sum(map(int, list(str(x ** n))))
