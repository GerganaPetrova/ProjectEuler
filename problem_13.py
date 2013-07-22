def halistone(n, count = 1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count 

maxi = [0,0]
for i in range(1000000):
    c = halistone(i)
    if c > maxi[0]:
        maxi[0] = c
        maxi[1] = i

print maxi 
