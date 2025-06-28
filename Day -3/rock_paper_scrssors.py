import random
rock = '''
       _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)

'''

paper = '''
      _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''

scissors = '''
        _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''

data = [rock, paper, scissors]

user = int(input("What do you want to choose? Type 0 from Rock, 1 for Paper and 2 for Scissors \n"))
if user >0 and user <=2:
 print(data[user])
 comp = random.randint(0, len(data)-1)
 print("Computer choose")
 print(comp)
 print(data[comp])



if user >=3 or user <0:
    print("You types a invalid number. You lose")
elif comp==user:
    print("It is a draw try again")
elif user ==0 and comp ==2:
    print("You win!")
elif comp ==0  and user ==2:
    print("You lose!")
elif comp>user:
    print("You lose!")
elif user>comp:
    print("You win!")


    
