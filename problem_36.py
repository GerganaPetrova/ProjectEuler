def is_palindrom(n):
    return str(n) == str(n)[::-1]

def double_base_numbers():
    result = 0
    for i in range(1,1000000):
        if is_palindrom(i) and is_palindrom(int(bin(i)[2:])):
            result += i

    return result


