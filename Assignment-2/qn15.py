"""
Create two sets, set_a and set_b, each with some common and some unique elements.
Write a program to find and print the symmetric difference of the two sets.
"""
set_a={1,"a",2,4,7,9}
set_b={2,"a","b",9}

difference=set_a.symmetric_difference(set_b)
print("The symmetrice difference is: ",difference)
