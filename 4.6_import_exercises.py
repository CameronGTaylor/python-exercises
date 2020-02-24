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
from statistics import mode
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

fruit_count = [fruit.count(fruit) for fruit in fruit_list]


print(len(users))
print(len(active_users))
print(len(inactive_users))
print(f"${sum(total_balance)}")
print(f"${sum(total_balance) / len(total_balance):.2f}")
print(user_min)
print(user_max)
print(mode(fruit_list))
print(fruit_count)
