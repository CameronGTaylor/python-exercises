#1
def is_two(number):
    return number in [2, '2']

vowels = ['a','e','i','o','u']
#2
def is_vowel(letter):
    return letter.lower() in vowels

#3
def is_consonant(letter):
    return not is_vowel(letter) 

#4
def capt(word):
    if is_consonant(word[0]) == True:
       return word.capitalize()
    else:
        return word

#5
def calculate_tip(tip, bill):
    if tip > 0 and tip < 1:
        return bill * tip + bill
    else:
        return "Tip must be percent between 0 and 1"

#6
def apply_discount(price, discount):
    if discount > 0 and discount < 1:
        return (1 - discount) * price
    else:
        return "Discount must be a percent between 0 and 1"

#7
def handle_commas(user_input):
    if "," in user_input:
        return int(user_input.replace(',', '_'))
    else:
        return "Your number must use commas"

#8
def get_letter_grade(grade):
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

#9
def remove_vowels(word):
    new_word = ""
    if word.isdigit() == False:
        for i in range(len(word)):
            if is_vowel(word[i]) == False:
                new_word = new_word + word[i]
    return new_word

#print(remove_vowels("what is happening"))

#10
# def normalize_name(user_string):
#     new_string = ''
#     unacceptable = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
#     if user_string.isdigit() == False:
#         for i in range(len(user_string)):
#             if user_string[i] not in unacceptable:
#                 new_string = new_string + user_string[i]
#                 #print(user_string[i])
#     return new_string

def normalize_name(user_string):
    unacceptable = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    if user_string.isdigit() == False:
        for letter in user_string:
            if letter in unacceptable:
                user_string = user_string.replace(letter,'')
        if ' ' in user_string:
            user_string = user_string.replace(' ','_')       
    return user_string.lower()

#11
def cumsum(user_list):
    total_list = []
    total = 0
    for num in user_list:
        total_list.append(total + num)
        total += num
    return total_list

print(cumsum([1,4,7,11]))