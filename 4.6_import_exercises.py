#1a
# import functions_exercises
# print(functions_exercises.cumsum([1,3,5]))
# 1b
# from functions_exercises import normalize_name
# print(normalize_name('823 wa^nt_ some@b*ody&^ to_ love'))
# # 1c
# from functions_exercises import capt as capitalize
# print(capitalize('bob barker'))

#1
# import itertools as it

# for i in it.product('abc','123'):
#     print(i)

# for i in it.permutations('ABCD', 2):
#     print(i)

from json import load
#from statistics import mode
from collections import Counter

profiles = load(open('profiles.json'))

users = [user['name'] for user in profiles]
active_users = [user['name'] for user in profiles \
    if user['isActive'] == True]
inactive_users = [user['name'] for user in profiles \
    if user['isActive'] == False]

total_balance_list = [user['balance'] for user in profiles]

total_balance = []
for word in total_balance_list:
    total_balance.append(float(word.replace(',', '').replace('$', '')))

max_balance = max(total_balance)
min_balance = min(total_balance)

for i in range(len(total_balance)):
    if total_balance[i] == max(total_balance):
        user_max = users[i]
    if total_balance[i] == min(total_balance):
        user_min = users[i]

fruit_list = [fruit['favoriteFruit'] for fruit in profiles]


fruit_count = Counter(fruit_list)
fruit_value = fruit_count.most_common()

# fruit_count = dict(Counter(fruit_list))

# fruit_value = []
# for fruit in fruit_count:
#     fruit_value.append(fruit_count.get(fruit))

# for fruit in fruit_count:
#     if fruit_count.get(fruit) == min(fruit_value):
#         min_fruit = fruit

all_greetings = [message['greeting'] for message in profiles]
all_greetings = ''.join(all_greetings)
all_greetings = all_greetings.split(' ')

new_greetings = []
for word in all_greetings: 
    if word.isdigit() == True:
        new_greetings.append(int(word))

print(len(users))
print(len(active_users))
print(len(inactive_users))
print(f"${sum(total_balance)}")
print(f"${sum(total_balance) / len(total_balance):.2f}")
print(f'The lowest balance user is {user_min}')
print(f'The highest balance user is {user_max}')
print(f'The most common fruit is {fruit_value[0][0]}')
print(f'The least common fruit is {fruit_value[-1][0]}')
# print(f'The most common fruit is {mode(fruit_list)}')
# print(f'The least common fruit is {min_fruit}')
print(f'The total number of unread messages ' \
     f'for all users is {sum(new_greetings)}')