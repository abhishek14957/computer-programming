#Write a function with keyword-only arguments (Python 3+).
def greet(*, name):
    return f"Hello, {name}!"
print(greet(name="Alice")) 