#1a
with open('4.6_import_exercises.py') as f:
    # file_contents = f.read()
    file_contents_lines = f.readlines()
#print(file_contents)

#1b
# for i in range(len(file_contents_lines)):
#     print(f'Line: {i} {file_contents_lines[i]}')

#2a
grocery_list = ['Eggs', 'Bread', 'Milk', 'Butter']
#2b
def make_grocery_list(user_list):
    with open('my_grocery_list.txt', 'w') as f:
        for item in user_list:
            f.writelines(item + '\n')

make_grocery_list(grocery_list)

#2c
def show_grocery_list(user_file):
    with open(user_file) as f:
        contents = f.readlines()
        contents = [content.replace('\n', '') for content in contents]
    print(contents)
    return contents

show_grocery_list('my_grocery_list.txt')

#2d
def buy_item(user_item):
    grocery_list = show_grocery_list('my_grocery_list.txt')
    for item in grocery_list:
        if user_item.lower() == item.lower():
            grocery_list.remove(item)
    print(grocery_list)
    return grocery_list

buy_item('milk')