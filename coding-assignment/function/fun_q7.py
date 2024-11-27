#Use a function as an argument to another function.
def apply_func(x, func):
    return func(x)
print(apply_func(5, lambda x: x ** 2))  