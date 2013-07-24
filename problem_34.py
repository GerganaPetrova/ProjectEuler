from math import factorial

def digit_factorials():
    result = []
    for i in range(3,40586):
        if sum(map(factorial,map(int, str(i)))) == i:
            result.append(i)
    return sum(result)
