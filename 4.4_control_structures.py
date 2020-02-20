#1a
# weekday = input("Enter the day of week: ")
# if weekday.lower() == "monday":
#     print("It is Monday my dudes")
# else:
#     print("It is not Monday")

#1b
# weekday = input("Enter the day of week: ")
# weekday_list = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# if weekday.lower() in (["saturday", "sunday"]):
#     print("It is the weekend, party hardy!")
# elif weekday.lower() in weekday_list:
#     print("Sadly it is still a weekday")
# else:
#     print("You gotta type a real day, friend")

#1c
# hours_worked = 46
# hourly_rate = 25
# if hours_worked <= 40:
#     weekly_pay = hours_worked * hourly_rate
# else:
#     weekly_pay = hours_worked * 1.5 * hourly_rate

#2a
# i = 5
# while i <= 15:
#     print(i)
#     i += 1

# i = 0
# while i <= 100:
#     print(i)
#     i += 2

# i = 100
# while i >= -10:
#     print(i)
#     i -= 5

# i = 2
# while i < 1000000:
#     print(i)
#     i **= 2

# i = 100
# while i > 0:
#     print(i)
#     i -= 5

#2b
# number = int(input("Please enter a number: "))
# for i in range(1,11):
#     print(f"{number} x {i} = ", number * i)
#     i += 1

# for i in range(1,10):
#     print(str(i) * i)
#     i += 1

#2c
# number = input('Please enter an odd number between 1 and 50: ')

# while True:
#     if (number.isdigit() == True and int(number) % 2 != 0 
#     and int(number) in range(1,51)):
#         break
        
#     else:
#         print("That is not an acceptable answer, Dave. Try again.")
#         number = input('Please enter an odd number between 1 and 50: ')

# i=1   
# while i < 50:
#     if i != int(number):
#         print("Here is an odd number: ", i)
#         i += 2
#     else:
#         print("Yikes! Skipping number: ", i)
#         i += 2
#         continue

#2d
# pos_number = input('Please enter a positive number: ')

# while True:
#     if pos_number.isdigit() == True and int(pos_number) > 0:
#         break
        
#     else:
#         print("That is not an acceptable answer, Dave. Try again.")
#         pos_number = input('Please enter a positive number: ')

# for i in range(0,int(pos_number)+1):
#     print(i)

# #2e
# for i in range(int(pos_number),0,-1):
#     print(i)

#3
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

#4
# while True:
#     user_int = input("What number would you like to go up to? ")
#     while True:
#         if user_int.isdigit() == True:
#             break
#         else:
#             print("That is not an acceptable answer, Dave. Try again.")
#             user_int = input('What number would you like to go up to? ')

#     print("\nHere is your table!\n\nnumber | squared | cubed")
#     for i in range(1,int(user_int) + 1):
#        print(f"{i}      | {i ** 2}       | {i ** 3}")

#     print("\n\n")
#     user_accept = input("Continue? Y or N: ")

#     if user_accept.lower() == 'y':
#         continue
#     else:
#         break

#5
# while True:
#     user_grade = input("Enter your grade: ")
#     while True:
#         if user_grade.isdigit() == True and int(user_grade) <= 100:
#             break
#         else:
#             print("That is not an acceptable answer, Dave. Try again.")
#             user_grade = input("Enter your grade: ")

#     user_grade = int(user_grade)
#     if user_grade <= 100 and user_grade > 88:
#         print("A\n")
#     elif user_grade >= 80 and user_grade < 88:
#         print("B\n")
#     elif user_grade >= 67 and user_grade < 80:
#         print("C\n")
#     elif user_grade >= 60 and user_grade < 67:
#         print("D\n")
#     else: 
#         print("F\n")

#     user_ready = input("Continue? Y or N: ")
#     if user_ready.lower() == 'y':
#         continue
#     elif user_ready.lower() == 'n':
#         break
#     else:
#         print("That is not an acceptable answer, Dave. Try again.")
#         user_ready = input("Continue? Y or N: ")

#6
my_books = [
    {
        "title": "Silmarillion",
        "author": "J R R Tolkien",
        "genre": "fantasy"
    }
    {
        "title": "Lord of the Flies",
        "author": "William Golding",
        "genre": "fantasy"
    }
    {
        "title": "Silmarillion",
        "author": "J R R Tolkien",
        "genre": "fantasy"
    }
    {
        "title": "Silmarillion",
        "author": "J R R Tolkien",
        "genre": "fantasy"
    }
]