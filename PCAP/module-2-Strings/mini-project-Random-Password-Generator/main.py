import random
import sys


def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "!@#$%&*^|()_+"

    password_length = int(input("Provide password length: "))
    use_uppercase = input("Use uppercase letters? (y/n): ").startswith("y")
    use_digits = input("Use digits? (y/n): ").startswith("y")
    use_special_characters = input("Use special characters? (y/n): ").startswith("y")

    possible_characters = letters

    if use_uppercase:
        possible_characters += letters.upper()

    if use_digits:
        possible_characters += digits

    if use_special_characters:
        possible_characters += special_characters

    password = ""

    for _ in range(password_length):
        password += random.choice(possible_characters)

    print("\nGenerated password:", password, "\n")


while True:
    choice = input(
        """-- Password generator --
Choose option:
1: generate password
2: exit the program
Your choice: """
    )

    if not choice.isnumeric() or int(choice) not in (1, 2):
        print("Please enter a correct value\n")
    elif int(choice) == 2:
        print("Bye!")
        sys.exit()
    else:
        generate_password()
