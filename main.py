# Password Generator Program - Python 3.14
# https://docs.python.org/3/library/secrets.html
# https://docs.python.org/3/library/string.html

# Libraries
import secrets
import string


# Password Generator
def generate_password():
    # Dictionary
    valid_passwords = {
        # Key              Value
        "uppercase(A-Z)": string.ascii_uppercase,
        "lowercase(a-z)": string.ascii_lowercase,
        "numbers(0-9)": string.digits,
        "punctuation(!@#$%^&*)": string.punctuation,
    }

    # Loops through the dictionary until the user picks at least one category
    character_pool = ""
    while not character_pool:
        for key, value in valid_passwords.items():
            user = input(f"Include {key}? (yes/no): ").strip().lower()
            if user == "yes" or user == "y":
                character_pool += value
        if not character_pool:
            print("Please enter a valid character")

    # Password Length & Error Validation
    while True:
        try:
            length = int(input("How many characters would you like to generate?: "))
            if length < 8 or length > 100:
                print("Please enter a number between 8 and 12")
            else:
                break
        except ValueError:
            print("Please enter a number between 8 and 12: ")


    # Amount of passwords generated
    while True:
        try:
            amount = int(input("How many passwords would you like to generate?: "))
            if amount > 0:
                break
            print("Please enter at least one character")
        except ValueError:
            print("Please enter a valid character")


    # Generate The Password
    for x in range(amount):
        password = ''.join(secrets.choice(character_pool) for _ in range(length))
        print(password)


# Main Program
if __name__ == "__main__":
    generate_password()
