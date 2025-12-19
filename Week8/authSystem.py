import hashlib
import json
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
users_file = os.path.join(script_dir, 'users.json')

class User:
    def __init__(self, username, password, privilege='user', hashed=False):
        self.username = username
        self.privilege = privilege
        if hashed:
            self.password = password
        else:
            self.password = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def register():
        while True:
            username = input("Enter username: ")
            if len(username) < 4:
                print("Username must be at least 4 characters long.")
                continue
            if not re.match("^[a-zA-Z0-9_]+$", username):
                print("Username can only contain alphanumeric characters and underscores.")
                continue
            try:
                with open(users_file, 'r') as f:
                    data = json.load(f)
                    if username in data:
                        print("Username already exists.")
                        continue
            except (FileNotFoundError, json.JSONDecodeError):
                pass
            break
        while True:
            password = input("Enter password: ")
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                continue
            if not re.search("[a-z]", password):
                print("Password must contain at least one lowercase letter.")
                continue
            if not re.search("[A-Z]", password):
                print("Password must contain at least one uppercase letter.")
                continue
            if not re.search("[0-9]", password):
                print("Password must contain at least one number.")
                continue
            if not re.search("[!@#$%^&*()_+= -{};:'<>,./?~`]", password):
                print("Password must contain at least one special character.")
                continue
            break
        
        try:
            with open(users_file, 'r+') as f:
                data = json.load(f)
                if not data: # if the file is empty
                    user = User(username, password, privilege='admin')
                else:
                    user = User(username, password)

                data[user.username] = {'password': user.password, 'privilege': user.privilege}
                f.seek(0)
                json.dump(data, f)
        except (FileNotFoundError, json.JSONDecodeError):
            # First user is an admin
            user = User(username, password, privilege='admin')
            with open(users_file, 'w') as f:
                json.dump({user.username: {'password': user.password, 'privilege': user.privilege}}, f)
        
        print("User registered successfully!")

    @staticmethod
    def login():
        while True:
            username = input("Enter username: ")
            if not username:
                print("Username cannot be empty.")
                continue
            break
        while True:
            password = input("Enter password: ")
            if not password:
                print("Password cannot be empty.")
                continue
            break
        
        try:
            with open(users_file, 'r') as f:
                data = json.load(f)
                if username in data:
                    user_data = data[username]
                    user = User(username, user_data['password'], user_data['privilege'], hashed=True)
                    if user.check_password(password):
                        print(f"Login successful! Welcome {user.username}. Your privilege level is: {user.privilege}")
                        return user
                    else:
                        print("Invalid credentials.")
                else:
                    print("User not found.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No users registered yet.")
        return None

    def promote(self):
        if self.privilege != 'admin':
            print("You do not have permission to promote users.")
            return

        while True:
            username_to_promote = input("Enter the username of the user to promote: ")
            if not username_to_promote:
                print("Username cannot be empty.")
                continue
            break
        
        try:
            with open(users_file, 'r+') as f:
                data = json.load(f)
                if username_to_promote in data:
                    if username_to_promote == self.username:
                        print("You cannot promote yourself.")
                        return
                    data[username_to_promote]['privilege'] = 'admin'
                    f.seek(0)
                    f.truncate()
                    json.dump(data, f, indent=4)
                    print(f"User {username_to_promote} has been promoted to admin.")
                else:
                    print("User not found.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No users registered yet.")

    def demote(self):
        if self.privilege != 'admin':
            print("You do not have permission to demote users.")
            return

        while True:
            username_to_demote = input("Enter the username of the user to demote: ")
            if not username_to_demote:
                print("Username cannot be empty.")
                continue
            break
        
        try:
            with open(users_file, 'r+') as f:
                data = json.load(f)
                if username_to_demote in data:
                    if username_to_demote == self.username:
                        print("You cannot demote yourself.")
                        return
                    data[username_to_demote]['privilege'] = 'user'
                    f.seek(0)
                    f.truncate()
                    json.dump(data, f, indent=4)
                    print(f"User {username_to_demote} has been demoted to user.")
                else:
                    print("User not found.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No users registered yet.")

    def information(self):
        match self.privilege:
            case 'admin':
                while True:
                    input_username = input("Enter username to get information: ")
                    if not input_username:
                        print("Username cannot be empty.")
                        continue
                    break
                try:
                    with open(users_file, 'r') as f:
                        data = json.load(f)
                        if input_username in data:
                            user_data = data[input_username]
                            print(f"Username: {input_username}, Privilege: {user_data['privilege']}")
                        else:
                            print("User not found.")
                except (FileNotFoundError, json.JSONDecodeError):
                    print("No users registered yet.")
            case 'user':
                print(f"Username: {self.username}, Privilege: {self.privilege}")


if __name__ == "__main__":
    logged_in_user = None
    while True:
        if logged_in_user:
            print(f"\nLogged in as {logged_in_user.username} ({logged_in_user.privilege})")
        
        print("1. Register")
        print("2. Login")
        if logged_in_user and logged_in_user.privilege == 'admin':
            print("3. Promote User")
            print("4. Demote User")
        print("5. Logout")
        print("6. Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            User.register()
        elif choice == 2:
            logged_in_user = User.login()
        elif choice == 3 and logged_in_user and logged_in_user.privilege == 'admin':
            logged_in_user.promote()
        elif choice == 4 and logged_in_user and logged_in_user.privilege == 'admin':
            logged_in_user.demote()
        elif choice == 5:
            logged_in_user = None
            print("Logged out.")
        elif choice == 6:
            if logged_in_user:
                logged_in_user.information()
            else:
                print("You need to log in first.")
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")
