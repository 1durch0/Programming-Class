user_pin = "272836"
attempts = 0
max_attempts = 3
login_successful = False

while attempts < max_attempts:
    print(f"Attempt {attempts+1} of {max_attempts}")
    entered_pin = input("Enter your pin: ")
    length_pin = len(str(entered_pin))
    if  length_pin == 6:
        if entered_pin == user_pin:
            login_successful = True
            print(f"You login was successful!")
            break
        else:
            attempts += 1
            print(f"Wrong pin. Try again.")
    else:
        attempts += 1
        print(f"Pin doesn't fit length requirement. Try again.")

if not login_successful == True:
    print("Login failed. No attempts left!")
