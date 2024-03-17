"""
Write a function list_to_set(input_list) that takes a
list as input and returns a set containing unique elements 
from the list.
"""

def list_to_set(input_list):
    sets=set(input_list)
    return sets

list=[1,6,4,3,5,6,33,2,8]
returned_list_to_set=list_to_set(list)
print("The Returned set is:",returned_list_to_set)