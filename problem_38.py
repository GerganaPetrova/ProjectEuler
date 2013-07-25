def is_pandigital(string):
    if len(string) > 9:
        return False
    digits = list(string)
    check = ['1','2','3','4','5','6','7','8','9']

    if sorted(digits) == check:
        return True
    return False

for n in range(9876, 9123, -1):
    p = str(n*1) + str(n*2)
    if is_pandigital(p):
        print p
        break
