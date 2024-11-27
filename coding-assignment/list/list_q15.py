#Copy a list (without affecting the original).
original_list = [1, 2, 3]
copied_list = original_list[:]
copied_list.append(4)
print(original_list)  
print(copied_list) 