#Use a function as a return value.
def multiplier(x):
    return lambda y: x * y
times_two = multiplier(2)
print(times_two(5))  