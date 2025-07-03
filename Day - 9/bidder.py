hammer = '''

       T                                    \`.    T
       |    T     .--------------.___________) \   |    T
       !    |     |//////////////|___________[ ]   !  T |
            !     `--------------'           ) (      | !
                                             '-'      !
'''

print(hammer)
users = {}

try_again = True

def bid_winner(data):
    big_bull = ""
    big_bid = 0
    for key in data:
        if data[key] > big_bid:
            big_bull = key
            big_bid =data[key]
    print(f" The {big_bull} is the winner of the BID with highest bidding ₹{big_bid}") 
        
while try_again:
    valid = True
    user_name = input("Enter your name \n")

    bid = int(input("Enter your bid amount \n"))
    users[user_name] = bid

    while valid:
        bid_choice = input("Is there any other player to bid, Type yes or no \n")

        if bid_choice in ["no",'yes']:
            if bid_choice== "yes":
                valid =False
                print("\n"*10)
            if bid_choice == "no":
                # print(users)
                bid_winner(users)
                valid =False
                try_again =False
        else:
            print("Please enter valid keyword to proceed.!")