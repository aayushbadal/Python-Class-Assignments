"""
Write a function remove_duplicates(input_list) that takes a list as an argument and
returns a new list with duplicates removed using a set.
"""

def remove_duplicates(input_list):
    unique_elements=set(input_list)
    return unique_elements

input= [1,3,5,3,5,5,7,4,7,5,7,5]
unique=list(remove_duplicates(input))
print("The list without duplication is:",unique)
