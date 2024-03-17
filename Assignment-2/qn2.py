"""
Write a function merge_dicts(dict1, dict2) that takes two dictionaries
as arguments and returns a new dictionary containing the combined key-value
pairs of both dictionaries. If there are common keys, the values from the
second dictionary should overwrite the values from the first dictionary.
Given the dictionary grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92},
write a program that calculates and prints the average grade.
"""

def merge_dicts(dict1,dict2):
    merged_dicts=dict1.copy()
    for key,value in dict2.items():
        merged_dicts[key]=value
    return merged_dicts


grade={"Alice": 90, "Bob": 85, "Charlie": 92}

grades2={"Ram": 50, "Shyam": 98, "Hari": 76}

merged_grades=merge_dicts(grade,grades2)

print("The merged dict is:",merged_grades)

total_grade=sum(merged_grades.values())
num_of_student=len(merged_grades)
avg_grade=total_grade/num_of_student
print("The average grade is",avg_grade)