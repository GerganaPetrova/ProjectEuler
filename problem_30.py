def digit_fifth_powers():
    result = 0
    for i in range(2, 354294):
        if i == sum(map((lambda x: x ** 5),map(int, str(i)))):
            result += i
    return result       
