import random
logo = '''
 ____  _       _     _           _    
| __ )| | __ _| |__ | | ___  ___| | __
|  _ \| |/ _` | '_ \| |/ _ \/ __| |/ /
| |_) | | (_| | |_) | |  __/\__ \   < 
|____/|_|\__,_|_.__/|_|\___||___/_|\_/
                                      

'''
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card = []
computer_card = []
def random_card():
    single = random.choice(card)
    return single

for _ in range(2):
    user_card.append(random_card())
    computer_card.append(random_card())

def calculate(card):
    if sum(card) == 21 and len(card) == 2:
        return 0

    if 11 in card and sum(card) >21:
        card.remove(11)
        card.append(1)    
    return sum(card)



user_score = -1
computer_score = -1

#comparing function
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🤔"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Win with the Blackjack 🥳"
    elif user_score > 21:
        return "Lose, opponent has a Blackjack 😥"
    elif computer_score >21:
        return "Opponent went over. You Win !😍"
    elif user_score > computer_score:
        return "You Win !😍"
    else:
        return "You lose 😤"
    

try_again = True

#main
while try_again:
    user_score =  calculate(user_card)
    computer_score = calculate(computer_card)

    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer card: {computer_card[0]}")
    print(computer_card)
    print(user_score)
    if user_score == 0 and computer_score ==0 and user_score < 21:
        try_again =False
    else:
        choice = input("Do you want to play a game pf Blackjack? Type 'y' for Yes or 'n' for No :")
        if choice in ['y', "n"]:
            if choice =="y":
                user_card.append(random_card())
            else:
                try_again=False
        else:
            print("Please enter valid input")

print(computer_score)

while computer_score !=0 and computer_score <17:
    computer_card.append(random_card())
    computer_score = calculate(computer_card)
    print("yaha aaya")


compare(user_score=user_score, computer_score=computer_score)