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

#1b
# weekday = input("Enter the day of week: ")
# day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# weekday_list = day_of_week[:5]
# weekend_list = day_of_week[5:]
# while weekday.lower() not in weekday_list and weekday.lower() not in weekend_list:
#     weekday = input("Enter the day of week: ")
# if weekday.lower() in weekend_list:
#     print("It is the weekend, party hardy!")
# elif weekday.lower() in weekday_list:
#     print("Sadly it is still a weekday") 

#1c
# hours_worked = 46
# hourly_rate = 25
# if hours_worked <= 40:
#     weekly_pay = hours_worked * hourly_rate
# else:
#     weekly_pay = ((hours_worked - 40) * 1.5 * hourly_rate) + (40 * hourly_rate)
# print(f"${weekly_pay}")


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


#2bi
# number = int(input("Please enter a number: "))
# for i in range(1,11):
#     print(f"{number} x {i} = ", number * i)
#     i += 1

#2bii
# for i in range(1,10):
#     print(str(i) * i)
#     i += 1


#2c
# number = input('Please enter an odd number between 1 and 50: ')

# while (number.isdigit() == False or int(number) % 2 == 0 
#   or int(number) not in range(1,50)):
#     print("That is not an acceptable answer, Dave. Try again.")
#     number = input('Please enter an odd number between 1 and 50: ')

# for i in range(1,50):
#     if i % 2 ==0:
#         continue
#     if i == int(number):
#         print("Yikes! Skipping number: ", i)
#         continue
#     print("Here is an odd number: ", i)


#2d
# pos_number = input('Please enter a positive number: ')

# while pos_number.isdigit() == False or int(pos_number) < 0:
#     print("That is not an acceptable answer, Dave. Try again.")
#     pos_number = input('Please enter a positive number: ')

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
#     user_int = input('Please enter an integer: ')

#     while user_int.isdigit() == False:
#         print("That is not an acceptable answer, Dave. Try again.")
#         user_int = input('Please enter an integer: ')

#     print("\nHere is your table!\n\nnumber | squared | cubed")
#     for i in range(1,int(user_int) + 1):
#         print(f"{i}      | {i ** 2}       | {i ** 3}")

#     print("\n")
#     user_accept = input("Continue? Y or N: ")

#     if user_accept.lower() != 'y':
#         print("Logging out")
#         break

#5
# while True:
#     user_grade = input('Please enter your grade: ')

#     while (user_grade.isdigit() == False 
#       or int(user_grade) not in range(0,101)):
#         print("That is not an acceptable answer, Dave. Try again.")
#         user_grade = input('Please enter your grade: ')

#     user_grade = int(user_grade)
#     if user_grade <= 100 and user_grade > 88:
#         print("A\n")
#     elif user_grade >= 80:
#         print("B\n")
#     elif user_grade >= 67:
#         print("C\n")
#     elif user_grade >= 60:
#         print("D\n")
#     else: 
#         print("F\n")

#     user_ready = input("Continue? Y or N: ")
#     if user_ready.lower() not in ['y', 'yes']:
#         break


#6
my_books = [
    {
        "title": "Silmarillion",
        "author": "J R R Tolkien",
        "genre": "fantasy"
    },
    {
        "title": "Lord of the Flies",
        "author": "William Golding",
        "genre": "fantasy"
    },
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "scifi"
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "scifi"
    },
    {
        "title": "The Republic",
        "author": "Plato",
        "genre": "philosophy"
    }
]

genres = set([book['genre'] for book in my_books])


print(f"\nAvailable genres are: {genres}")
user_question = input("\nWhat genre are you interested in? ")
while (user_question not in genres):
    print("That is not an acceptable answer, Dave. Try again.")
    user_question = input("\nWhat genre are you interested in? ")

for book in my_books:
    if user_question == book['genre']:
        print(book['title'])