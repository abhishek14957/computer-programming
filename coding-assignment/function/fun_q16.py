#Use a function with map.
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4]
print(list(map(square, numbers)))  