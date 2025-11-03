passwords = [
    "password",
    "1234567",
    "S3CreT",
    "L?38NblD94",
    "PASSWORD",
]

def check_password(password_list):
    password_validation = {}

    for pwd in password_list:
        # default case
        is_valid = True

        # Must be at least 8 characters
        if len(pwd) <= 7:
            is_valid = False
        # Must contain an uppercase letter
        elif not any(char.isupper() for char in pwd):
            is_valid = False
        # Must contain a digit
        elif not any(char.isdigit() for char in pwd):
            is_valid = False

        password_validation[pwd] = is_valid

    # Display results
    for pwd, valid in password_validation.items():
        print(f"{pwd}: {valid}")

check_password(passwords)
