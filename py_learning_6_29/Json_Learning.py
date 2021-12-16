import json


def get_stored_name():
    filename = 'user_name.json'
    try:
        with open(filename) as name_file:
            user_name = json.load(name_file)
    except FileNotFoundError:
        return None
    else:
        return user_name


def greet_user():
    user_name = get_stored_name()
    if user_name:
        print("Welcome back, " + user_name + "!")
    else:
        user_name = input("What's your name? ")
        filename = 'user_name.json'
        with open(filename, 'w') as name_file:
            json.dump(user_name, name_file)
            print("We will remember you when you come back, " + user_name + "!")
