#Use default arguments in a function.
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())         
print(greet("Alice")) 