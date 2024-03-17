
a=int(input("Enter value for A : "))
b=int(input("Enter value for B : "))
print("Choose:\n + for addition\n - for subtraction\n * for multiplication\n / for division.")
choice=input("Enter your choice:")
if(choice=='+'):
    print(f"The addition of {a} and {b} is {a+b}.")
elif(choice=='-'):
    print(f"The subtraction of {a} and {b} is {a-b}.")
elif(choice=='*'):
    print(f"The multiplication of {a} and {b} is {a*b}.")
elif(choice=='/'):
    print(f"The division of {a} and {b} is {a/b}.")
else:
    print("Invalid choice.Strat from begining.")