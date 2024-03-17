num=[]
i=0
e=(int(input("Enter the number of elements:")))
while(i<e):
    n=int(input(f"Enter number({i+1}):"))
    i+=1
    num.append(n)
sum=0
print("The Entered list is:")
print(num)
for i in num:
    sum=sum+i
print(f"The sum of the elements in {num} is {sum}.")