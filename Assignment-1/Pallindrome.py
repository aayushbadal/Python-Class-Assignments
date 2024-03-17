original_string=input("Enter the string:")
reversed_string=""
l=len(original_string) -1
while l>=0:
    reversed_string+=original_string[l]
    l-=1

if(original_string==reversed_string):
    print("Yes the given string is palindrome.")
else:
    print("No! the given string is not a palindrome.")