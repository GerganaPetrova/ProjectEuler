def count_digits(n):
    return len(str(n))

def fib_gen():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def digits_fib(n):
    f = fib_gen()
    x = f.next()
    counter = 0
    while count_digits(x) < n:
        x = f.next()
        counter += 1
    return counter
         

