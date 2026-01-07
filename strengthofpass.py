import re

def password_strength(password):
    if len(password)<8:
        print("Password is too short")
    elif not re.search("[a-z],password"):
        print("Password should have atleast one lowercase letter")
    elif not re.search("[A-Z],password"):
        print("Password should have atleast one uppercase letter")   
    elif not re.search("[0-9]",password):
        print("Password should have atleast one digit")
    elif not re.search("[!@#$%^&*(),.?\'':{}|<>]",password):
        print("Password should have at least one special character")
    else:
        print("Password is strong")

user_password = input("Enter a password to check its strength:")
password_strength(user_password)