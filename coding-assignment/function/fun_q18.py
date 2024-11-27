#Write a function that modifies a mutable argument.
def add_item(lst, item):
    lst.append(item)
my_list = [1, 2]
add_item(my_list, 3)
print(my_list)  