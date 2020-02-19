

username = 'codeup'
password = 'notastrongpassword '
def checks(username, password):
    if (
    len(password) >= 5 and
    len(username) <= 20 and 
    password != username and
    username == username.strip() and
    password == password.strip()) :
        return "Success"
    else:
        return "Try a different username/password combo"

print(checks(username, password))