from math import factorial

#The number of how many routes we have can be found by
#finding how many combinations of 20 right moves we can have in our 40 moves:
def count_paths():
    return factorial(40) / (factorial(20) * factorial(20))

print count_paths()    
