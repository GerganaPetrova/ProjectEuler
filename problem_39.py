def help_dict(d):
    max = 0
    for key in d.keys():
        if d[key] > max:
            max = d[key]
            k = key
    return k

def int_right_triangles():
    result = {}
    for a in range(1,1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c <= 1000:
                   if result.has_key(a+b+c):
                        result[a+b+c] += 1
                   else:
                        result[a+b+c] = 1
    return help_dict(result) 
