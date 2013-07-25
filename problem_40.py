def irrational_decimal_fraction():
    s = ''
    for i in range(1000000):
       s = s + str(i)
       if len(s) > 1000000:
           break
    answer = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
    return answer

            
