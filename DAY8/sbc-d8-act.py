def users_file():
    try:
        with open("users.txt", "r") as file:
            users = {}
            for line in file:
                username, password = line.strip().split(",")
                users[username.split(":")[1].strip()] = password.split(":")[1].strip()
            return users
    except FileNotFoundError:
        return {}

def users_to_file(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"username: {username}, password: {password}\n")

def register(users):
    print("\n" + "_" * 20 + "REGISTER" + "_" * 20)
    username = input("Enter a username: ")
    if username in users:
        print("\tUsername already exists. Please choose a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    users_to_file(users)
    print("\tRegistration successful!\n")

def login(users):
    print("\n" + "_" * 20 + "LOGIN" + "_" * 20)
    username = input("Enter your username: ")
    if username not in users:
        print("\tUsername not found. Please register first.")
        return
    password = input("Enter your password: ")
    if password != users[username]:
        print("\tIncorrect password. Try again.")
        return
    print("\tLogin successful!\n")

def change_password(users):
    print("\n" + "_" * 20 + "CHANGE PASSWORD" + "_" * 20)
    username = input("Enter your username: ")
    if username not in users:
        print("\tUsername not found. Please register first.")
        return
    old_password = input("Enter your current password: ")
    if old_password != users[username]:
        print("\tIncorrect password. Try again.")
        return
    new_password = input("Enter your new password: ")
    users[username] = new_password
    users_to_file(users)
    print("\tPassword changed successfully!\n")

def main():
    users = users_file()
    while True:
        print("\n" + "_" * 20 + "MAIN MENU" + "_" * 20)
        print("1. Register".center(32))
        print("2. Log in".center(30))
        print("3. Change password".center(38))
        print("4. Quit".center(27))
        choice = input("Enter your choice: ")
        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            change_password(users)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.\n".center(47))

if __name__ == "__main__":
    main()