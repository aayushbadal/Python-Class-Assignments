"""
Given a tuple with repeated elements, write a program 
to count the occurrences of a specific element within
the tuple.
"""

def occurence_count(input,target):
    occurence=input.count(target)
    return occurence

input_element=(1,2,4,3,2,4,3,2)
repeated_element=3

count=occurence_count(input_element,repeated_element)
print(f"The occurence of {repeated_element} is: {count}")