#Use a function to modify a global variable.
count = 0
def increment():
    global count
    count += 1
increment()
print(count)  