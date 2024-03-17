seq=[0,1]
i=0
a=0
b=1
t=int(input("Enter the number of terms:"))
print(a)
while(i!=t):
    c=a+b
    a=b
    b=c
    seq.append(c)
    i+=1
print(seq)