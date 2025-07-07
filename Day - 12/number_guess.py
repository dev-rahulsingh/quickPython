import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
guess  = input("Choose the difficulty. Type 'easy or 'hard : ")


final_number = random.randint(1, 100)
print(final_number)

def number_game (chance, final):
    if chance > 0:
        while chance:
            print(f"You have {chance} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess == final:
                print("You win. ! 🥳 ")
                chance = 0
            elif guess > final:
                print("Too high")
                chance-=1
            else:
                print("Too Low")
                chance-=1
    elif chance == 0:
        print("You've run out of guesse, You lose. 😓")

if guess in ["easy","hard"] :
    if guess == "easy":
        number_game(10, final=final_number)
    else:
        number_game(1, final=final_number)
else:
    print("Please write the correct word")