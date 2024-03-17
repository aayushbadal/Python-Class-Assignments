original_string=input("Enter the string:")
reversed_string=""
l=len(original_string) -1
while l>=0:
    reversed_string+=original_string[l]
    l-=1


print("Original String:",original_string)
print("Reversed String:",reversed_string)
