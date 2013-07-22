sum_of_squares = reduce((lambda x,y: x + y),map((lambda x: x * x), range(1,101)))
sums = sum(range(1,101))

result = sums ** 2 - sum_of_squares
print result
