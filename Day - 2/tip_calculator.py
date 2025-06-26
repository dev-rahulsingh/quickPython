print("Welcome to the tip Calculator")

bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10, 12, or 15"))
people = int(input("How many people to split  the bills?"))

final = (bill + (bill*tip/100))/people

print(f"Each person should pay: {final}")
                                                                           