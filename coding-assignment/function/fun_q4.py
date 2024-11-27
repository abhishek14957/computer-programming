#Create a function with variable-length arguments (*args).
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))  