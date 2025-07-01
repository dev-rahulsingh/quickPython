import random
# from xyzFile import logo              ---> Syntax

hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

letters = ["rahul", "pankaj", "jerry"]

index = random.randint(0,len(letters)-1)

lives = 6

# Inject logo through import
# print(logo)

chosse =letters[index]
print(chosse)

game_over = False
final_letter = []

while not game_over:
    print(f"****************************** {lives}/6 LIVES LEFT ******************************")
    char = input("Guess a character\n")

    # check that the letter is already guesses or not
    if char in final_letter:
        print(f"You've already guessed {char}")

    saved_letter =""

    for el in chosse:
        if char == el:
            saved_letter +=el
            final_letter.append(el)
        elif el in final_letter:
            saved_letter +=el
        else:
            saved_letter +="_"
        
    print(saved_letter)

    #if the letter is not the already guess in final word so we can let them know that they are in right track
    if char not in chosse:
        lives -=1
        print(f"You guessed {char}, that is not in the word. You lose a life.")
        if lives == 0:
            game_over =True
            print(f"******************** IT WAS {final_letter}, You LOSE.! **********************")

    if "_" not in saved_letter:
        game_over =True
        print("************************ You WIN! ***********************")

    print(hangman_stages[lives])