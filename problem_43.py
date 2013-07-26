import itertools

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

def check_properties(n):
    digits = n
    if int(digits[1]) * int(digits[2]) * int(digits[3]) % 2 == 0:
        if int(digits[2]) * int(digits[3]) * int(digits[4]) % 3 == 0:
            if int(digits[3]) * int(digits[4]) * int(digits[5]) % 5 == 0:
                if int(digits[4]) * int(digits[5]) * int(digits[6]) % 7 == 0:
                    if int(digits[5]) * int(digits[6]) * int(digits[7]) % 11 == 0:
                        if int(digits[6]) * int(digits[7]) * int(digits[8]) % 13 == 0:
                            if int(digits[7]) * int(digits[8]) * int(digits[9]) % 17 == 0:
                                return True

def sum_pandigitals():
    x = itertools.permutations('0123456789', 9)
    result = []
    for i in x:
        if is_pandigital(i,9) and check_properties(i):
            result.append(i)
    return sum(result)   
