import random
# # name = len(input("Enter your name"))

# # print( f"Number of Letters in youe name: {name}")
# random_number = random.randint(1,10)


# print(random_number) 


# friend = ["Ravi", "Ram","rahona","ramesh","raza"]

# num = random.randint(0, len(friend))
# print(friend[num])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])


# *** Loops ***
# for number in range (1,100):
#     if number%3 == 0 and number%5==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)


#Dictionary = Object

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] >=91:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] >=81 and student_scores[key]<=90:
#         student_grades [key] = "Exceeds Expectations"
#     elif student_scores[key] >=71 and student_scores[key]<=80:
#         student_grades  [key] = "Acceptable"
#     else:
#          student_grades[key] = "Fail"
         
# print(student_grades)


# def is_leap_year(year):
#     data = 0
#     if year % 4 == 0:
#         data += 1
        
#         if year % 100 == 0:
#             data -= 1
            
#             if year % 400 == 0:
#                 data += 1
                
#     else:
#         print("Not divisible by 4 → Not a leap year")
#     return data


# provided_year = int(input("Enter the year to check if it is a Leap Year:\n"))

# result = is_leap_year(provided_year)

# if result > 0:
#     print(f"The year {provided_year} is a Leap Year.")
# else:
#     print(f"The year {provided_year} is NOT a Leap Year.")

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.color("cyan4")
timmy.shape("turtle")

my_screen = Screen()
print(my_screen.canvheight)


my_screen.exitonclick()