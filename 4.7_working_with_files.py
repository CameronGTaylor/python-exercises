#1a
with open('4.6_import_exercises.py') as f:
    # file_contents = f.read()
    file_contents_lines = f.readlines()
#print(file_contents)

#1b
# for i in range(len(file_contents_lines)):
#     print(f'Line: {i + 1} {file_contents_lines[i]}')

#2a
grocery_list = ['Eggs', 'Bread', 'Milk', 'Butter']
#2b
def make_grocery_list(user_list):
    with open('my_grocery_list.txt', 'w') as f:
        for item in user_list:
            f.write(item + '\n')

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
    updated_groceries = show_grocery_list('my_grocery_list.txt')
    for item in updated_groceries:
        if user_item.lower() == item.lower():
            updated_groceries.remove(item)
    print(updated_groceries)
    make_grocery_list(updated_groceries)

buy_item('milk')

buy_item('bread')