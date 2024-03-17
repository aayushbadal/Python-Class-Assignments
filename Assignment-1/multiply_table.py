n=int(input("Enter the number that you want to find the multiplication table of: "))
i=1
print(f"\nThe Multiplication table of {n}:")
while(i<=10):
    m=n*i
    print(f"{n} X {i} = {m}")
    i+=1