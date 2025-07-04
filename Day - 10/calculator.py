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

first_try = True

while first_try:
    first_number = float(input("Enter the first number? :"))
    for sym in symbol:
        print(sym)
    final = 0
    try_again = True
    while try_again:
    
        operation = input("Pick an operation : ")
        if operation in symbol:
            second_number = float(input("What's the second number? :"))
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
            print(f"{first_number}{operation}{second_number} = {final}")
        else:
            print("Please Enter the valid symbols. !")
        more = input(f"Type 'y'to continue calculating with {final}, or type 'n' to start a new  calculation: ")
        if more in ["y", "n"]:
            if more == "y":
                first_number = final
            elif more =="n":
                try_again =False
                first_try =False
                print(f"The Final answer of the calculation is {final}")
                print("\n"*20)
        else:
            print("Please enter the valid keyword.!")