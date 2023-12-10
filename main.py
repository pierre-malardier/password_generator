# programme that create a password manager, one fonction that create the password,
# one that verify the strength of the password
# one that check if the password is already in the password.json file if it exist if not create it
# one that save the password in the password.json file

import random
import json
import pyperclip
import string

# function that create the password
def create_password():
    password = []
    for i in range(0, 4):
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
    random.shuffle(password)
    password = "".join(password)
    return password

# function that verify the strength of the password
def verify_password(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    else:
        return True
    
# function that check if the password is already in the password.json file if it exist if not create it

def check_password():
    try:
        with open("password.json", "r") as file:
            password = json.load(file)
    except FileNotFoundError:
        password = {}
    return password

# function that save the password in the password.json file

def save_password(password):
    with open("password.json", "w") as file:
        json.dump(password, file, indent=4)

# main function

def main():
    password = check_password()
    website = input("Enter the website: ")
    if website in password:
        print(f"The password for {website} is {password[website]}")
        pyperclip.copy(password[website])
    else:
        password[website] = create_password()
        save_password(password)
        print(f"The password for {website} is {password[website]}")
        pyperclip.copy(password[website])

main()
