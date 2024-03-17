"""
Write a function concat_tuples(tuple1, tuple2) that takes two tuples as arguments and returns a new tuple
containing elements from both tuples.
"""

def concat_tuples(tuple1,tuple2):
    tuple=tuple1+tuple2
    return tuple

tuple1=("1","2","3")
tuple2=("x","y","z")
tuple=concat_tuples(tuple1,tuple2)
print("the concatenated tuple is :",tuple)