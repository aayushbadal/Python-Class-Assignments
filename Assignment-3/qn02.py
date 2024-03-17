#   Write a function called is_palindrome that takes a string as input and returns True if 
#   the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def is_palindrome(original_string):
    reversed_string=""
    l=len(original_string)-1
    while(l>=0):
        reversed_string+=original_string[l]
        l-=1
    return original_string==reversed_string

string=str(input("Enter a string:"))
result=is_palindrome(string)
print(f"\tIs {string} palindrome?\n\tAns:{result}.")