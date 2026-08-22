"""
def greetings():
    print("Hello, Welcome to our class!")
def say_name(name):
    print("Hello" + name)
greetings()
say_name(" Leke")
"""
def welcome_message():
    print("\nWelcome to our platform please proceed to by creating an account \n")

def register_user():
    print("\n REGISTRATION FORM\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    email = input("Enter your email: ")
    if password == confirm_password:
        print("Registration successful")
        login(name, password)
        return name, password, email
    else:
        print("Registration failed, password does not match")
        return None, None, None

def login(name, password):
    print("\n Login Form\n")
    name_login = input("Enter your name: ")
    password_login = input("Enter your password: ")
    if name == name_login and password == password_login:
        print("Login successful")
        return True
    else:
        print("Login failed, either name or password is incorrect")
        return False

def main():
    welcome_message()
    register_user()
main()
