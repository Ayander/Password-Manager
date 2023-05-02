import string

class BasePasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):
        return password == self.get_password()

class PasswordManager(BasePasswordManager):
    def __init__(self):
        super().__init__()

    def set_password(self, new_password):
        if len(new_password) >= 6 and self.check_security_level(new_password) > self.get_level():
            if self.get_level() < 2 or (self.get_level() == 2 and self.check_security_level(new_password) == 2):
                self.old_passwords.append(new_password)
                return True
        return False

    def get_level(self):
        return self.check_security_level(self.get_password())

    def check_security_level(self, password):
        has_alpha = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        if has_alpha and has_digit and has_special:
            return 2
        elif has_alpha and has_digit:
            return 1
        else:
            return 0

def main():
    password_manager = PasswordManager()
    password_manager.old_passwords = ["simplePassword1"]

    while True:
        print("\nMenu:")
        print("1. View current password")
        print("2. Change password")
        print("3. Check password security level")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Current Password:", password_manager.get_password())
        elif choice == "2":
            new_password = input("Enter the new password: ")
            if password_manager.set_password(new_password):
                print("Password changed successfully!")
            else:
                print("Failed to change password.")
        elif choice == "3":
            print("Security Level:", password_manager.get_level())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
