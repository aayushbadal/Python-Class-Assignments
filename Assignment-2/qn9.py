"""
Create a nested dictionary called students with keys as student names and values as
dictionaries containing 'age' and 'grade' for each student. Add information for at least three students. 
"""

students={
    "Ram":{"age":19,"grade":"A+"},
    "Shyam":{"age":20,"grade":"B+"},
    "Hari":{"age":18,"grade":"A"}
}

for k,v in students.items():
    print("The name of student is:",k)
    print(f"Age :{v['age']}")
    print(f"Grade :{v['grade']}")