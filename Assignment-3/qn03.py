#Write a function called max_of_three that takes three numbers as input and returns the largest one.

def max_of_three(a,b,c):
    return max(a,b,c)

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
result=max_of_three(a,b,c)
print(f"\tThe largest is {result}.")