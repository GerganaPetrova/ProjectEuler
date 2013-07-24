def is_pandigital(string):
    if len(string) > 9:
        return False
    digits = list(string)
    check = ['1','2','3','4','5','6','7','8','9']

    if sorted(digits) == check:
        return True
    return False


def pandigital_numbers():
    products = set()
    for a in xrange(1,100):
        for b in xrange(a,6789):
            if len(str(a) + str(b) + str(a*b)) > 9:
                break
            if is_pandigital(str(a*b) + str(a) + str(b)):
                products.add(a*b)
    return sum(products)     
