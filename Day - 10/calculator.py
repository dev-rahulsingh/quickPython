logo = '''
 _____________________
|  _________________  |
| | RahulpY      0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
symbol = ["+", "-","*","/"]

first_number = int(input("Enter the first number? :"))
for sym in symbol:
    print("sym \n")
final = 0
try_again = True
while try_again:
    
    operation = input("Pick an operation : ")
    if operation in symbol:
        second_number = int(input("What's the second number? :"))
        if operation == "+":
            final = first_number + second_number
        elif operation == "-":
            final = first_number - second_number
        elif operation == "*":
            final = first_number * second_number
        elif operation == "/":
            if second_number != 0:
                final = first_number / second_number
            else:
                print("Cannot divide by zero.")


        print(f"{first_number}{operation}{second_number} = ")
    else:
        print("Please Enter the valid symbols. !")
