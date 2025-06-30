import random
letters = ["rahul", "pankaj", "jerry"]

index = random.randint(0,len(letters)-1)
chosse =letters[index]
print(chosse)


char = input("Guess a character\n")
final = ""
for el in chosse:
    if char ==el:
        final +=char
    else:
        final += '''_'''
print(final)