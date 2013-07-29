def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def check_number(n):
    counter = 0
    while not counter == 50:
        next_num = n + int(str(n)[::-1])
        if is_palindrome(next_num):
            return False 
        else:
             n = next_num
        counter += 1
    return True

def luchrel_numbers():
    res = 0 
    for i in range(10, 10001):
        if check_number(i):
            res += 1
    return res        
    
        
