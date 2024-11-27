#Create a function that uses zip to combine two lists.
def combine_lists(keys, values):
    return dict(zip(keys, values))
print(combine_lists(['a', 'b'], [1, 2]))