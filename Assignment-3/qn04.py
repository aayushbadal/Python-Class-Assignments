#   Write a function called is_prime that takes an integer as input
#   and returns True if the number is prime, and False otherwise.

def is_prime(number):
    count=0
    i=2
    while(i<number-1):
        if number % i == 0:
            count=1
            break
        i+=1
    return count==0

integer=int(input("Enter a number:"))
result=is_prime(integer)
print(f"\tIs {integer} prime?\n\tAns:{result}.")