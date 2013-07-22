def is_palindrome(x):
    return str(x) == str(x)[::-1]

n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n and is_palindrome(x):
            n = a * b
print n
                
