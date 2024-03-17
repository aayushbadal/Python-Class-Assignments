word=str(input("Enter a string: "))
l=len(word)
i=0
vowel_count=0
while(i!=l):
    w=word[i]
    if(w=="a" or w=="e" or w=="i" or w=="o" or w=="u"):
        vowel_count+=1
    i+=1
print(f"The total no of vowel in string [{word}] is {vowel_count}.")