import string
from passwordsData import passwords

def check_min_length(password, min_length=8):
    return len(password) >= min_length

def check_max_length(password, max_length=16):
    return len(password) <= max_length

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    return any(char in string.punctuation for char in password)

def validate_password(password):
    is_valid = True
    password_validation = {}
    if not check_min_length(password):
        is_valid = False
    if not check_max_length(password):
        is_valid = False
    if not check_uppercase(password):
        is_valid = False
    if not check_lowercase(password):
        is_valid = False
    if not check_digit(password):
        is_valid = False
    if not check_special_char(password):
        is_valid = False
    
    if is_valid == True:
        password_validation[password] = True
    else:
        password_validation[password] = False

    print(f"{password}: {password_validation[password]}")

for key in passwords.keys():
    validate_password(key)

