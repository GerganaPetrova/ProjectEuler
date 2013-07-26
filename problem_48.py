def last_ten_digits():
    n = str(sum(i ** i for i in range(1, 1001)))
    return n[len(n) - 10:]
