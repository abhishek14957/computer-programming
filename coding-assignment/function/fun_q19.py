#Write a function that uses try...except to handle errors.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
print(divide(10, 0)) 