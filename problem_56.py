def digits_sum(num):
    return sum(map(int,str(num)))

def powerful_digit_sum():
    max_sum = 1
    for a in range(100):
        for b in range(100):
            d = digits_sum(a ** b)
            if d > max_sum:
                max_sum = d
    return max_sum  
