#Create a decorator function.
def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper


@decorator
def say_hello():
    print("Hello!")
say_hello()