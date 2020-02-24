#1
def is_two(number):
    return number in [2, '2']

vowels = ['a','e','i','o','u']
#2
def is_vowel(letter):
    letter = letter.lower()
    return letter.isalpha() and letter.lower() in vowels\
        and len(letter) == 1

#3
def is_consonant(letter):
    if letter.isalpha() == True:
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
                new_word += word[i]
    return new_word

def remove_vowels2(word):
    new_word = ''.join(letter for letter in word \
                            if not is_vowel(letter))
    return new_word
#print(remove_vowels2("what is happening"))

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
    #isalnum and isidentifier
    if user_string.isdigit() == False:
        for letter in user_string:
            if letter in unacceptable:
                user_string = user_string.replace(letter,'')
        if ' ' in user_string:
            user_string = user_string.strip().replace(' ','_')       
    return user_string.lower()

#11
def cumsum(user_list):
    total_list = []
    total = 0
    for num in user_list:
        total_list.append(total + num)
        total += num
    return total_list

#Bonus 1
def twelveto24(user_time):
    while len(user_time) not in [6,7]:
        return "Enter a time in format (10:45am or 4:30pm)"
    if 'am' in user_time:
        if user_time[1] == '2':
            # user_time = user_time.split(':')
            # return f"00{user_time[1].split('am')[0]}"
            user_time = user_time.replace('12','00')
            user_time = user_time.split('am')
            return user_time[0]
        else:
            user_time = user_time.split('am')
            return user_time[0]
    elif 'pm' in user_time:
        user_time = user_time.split(':')
        user_time[0] = str(int(user_time[0]) + 12)
        user_time = ':'.join(user_time)
        user_time = user_time.split('pm')
        return user_time[0]
    else:
        return "Enter a time in format (10:45am or 4:30pm)"

print(twelveto24('12:30am'))

def col_index(column):
    total = 0
    column = column.lower()
    
    for i in range(0,len(column)):
        total += (ord(column[i]) - 96) * (26 ** (len(column)-1-i) )
    return total
