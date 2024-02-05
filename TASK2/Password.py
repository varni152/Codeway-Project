import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = ''

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_type():
    print("Choose the password complexity:")
    print("1. Easy (only lowercase letters)")
    print("2. Medium (lowercase and uppercase letters)")
    print("3. Strong (letters and digits)")
    print("4. Ultra (letters, digits, and special characters)")
    print("5. Custom (choose specific character types)")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def get_custom_options():
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    length = get_password_length()

    return include_lowercase, include_uppercase, include_digits, include_special_chars, length

def main():
    while True:
        password_type = get_password_type()

        if password_type == 5:
            include_lowercase, include_uppercase, include_digits, include_special_chars, length = get_custom_options()
        else:
            include_lowercase = (password_type == 1)
            include_uppercase = (password_type == 2 or password_type == 5)
            include_digits = (password_type == 3 or password_type == 5)
            include_special_chars = (password_type == 4 or password_type == 5)
            length = get_default_password_length(password_type)

        password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)
        print("Generated Password:", password)

        another_password = input("Do you want another password? (y/n): ").lower()
        if another_password != 'y':
            print("Thanks! For Wist")
            break

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive password length.")
        except ValueError:
            print("Please enter a valid number for the password length.")

def get_default_password_length(password_type):
    # Default lengths for each password type
    default_lengths = {1: 8, 2: 10, 3: 12, 4: 14, 5: 8}
    return default_lengths.get(password_type, 8)

if __name__ == "__main__":
    main()
