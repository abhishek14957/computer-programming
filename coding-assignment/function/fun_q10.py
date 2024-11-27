#Write a function with positional-only parameters (Python 3.8+).
def divide(a, b, /):
    return a / b
print(divide(10, 2)) 
