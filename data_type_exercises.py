

username = 'codeup'
password = 'notastrongpassword'
def checks(username, password):
    if (
    len(password) >= 5 and
    len(username) <= 20 and 
    password != username and
    username[0] == username.strip()[0] and
    password[0] == password.strip()[0] and 
    username[-1] == username.strip()[-1] and
    password[-1] == password.strip()[-1]) :
        return "Success"
    else:
        return "Try a different username/password combo"

print(checks(username, password))