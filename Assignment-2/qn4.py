"""
Write a function swap_elements(tuple_var) 
that takes a tuple as an argument and returns
a new tuple where the first and last elements are
swapped.
"""

def swap_elements(tuple_var):
    temp=tuple_var[0]
    tuple_var[0]=tuple_var[-1]
    tuple_var[-1]=temp
    return tuple_var()

tuples=("Ram","90","4.5")
swapped=swap_elements(tuples)
print("The swapped tuples is:",swapped)