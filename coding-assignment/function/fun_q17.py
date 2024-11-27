#Use a function with filter.
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4]
print(list(filter(is_even, numbers)))