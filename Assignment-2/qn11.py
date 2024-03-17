"""
Given a list of names, create a dictionary where the keys are names and the values are the lengths of the 
corresponding names.
"""

names=["Ram","Shyam","Hari"]

names_length_dict=[]
for i in names:
    name_length=len(i)
    names_length_dict.append(name_length)

print("The List of names is:",names)
print("The List is:",names_length_dict)