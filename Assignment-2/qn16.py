"""
Given three sets, set1, set2, and set3, write a program to find 
and print the intersection of all three sets.
"""

set1={1,2,5,3,8}
set2={9,4,7,3}
set3={5,7,6,5,3}

set_intersection=set1 & set2 & set3

print("The intersection is:",set_intersection)