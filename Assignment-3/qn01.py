#   Write a function called is_even that takes an integer 
#   as input and returns True if the number is even, and False otherwise.

def is_even(number):
    return number%2==0

n=int(input("Enter a number:"))
result=is_even(n)
print(f"\tIs {n} even?\n\tAns: {result}.")