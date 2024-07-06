import random
import string
import pyperclip

def generate_password(length, special_chars='', include_upper=True, include_lower=True, include_digits=True):
    characters = ''
    
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    
    if special_chars:
        characters += special_chars
    
    if not characters:
        raise ValueError("No characters to choose from for password generation.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_special_characters():
    special_chars = string.punctuation
    print(f"Available special characters: {special_chars}")
    selected_chars = input("Enter the special characters you want to include (e.g., @#$%&*), or press Enter to include all: ").strip()
    
    if not selected_chars:
        return special_chars
    
    # Validate the entered characters
    invalid_chars = [char for char in selected_chars if char not in special_chars]
    if invalid_chars:
        print(f"Warning: The following characters are not in the standard special characters set and will be ignored: {''.join(invalid_chars)}")
        selected_chars = ''.join([char for char in selected_chars if char in special_chars])
    
    return selected_chars

def get_valid_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        else:
            print("Invalid response. Please enter 'yes', 'no', 'y', or 'n'.")

def get_inclusion_options():
    include_upper = get_valid_input("Include uppercase letters? (yes/no or y/n): ")
    include_lower = get_valid_input("Include lowercase letters? (yes/no or y/n): ")
    include_digits = get_valid_input("Include digits? (yes/no or y/n): ")
    return include_upper, include_lower, include_digits

def generate_basic_password(length):
    # Basic mode includes uppercase, lowercase, digits, and special characters
    special_chars = string.punctuation
    include_upper = True
    include_lower = True
    include_digits = True
    return generate_password(length, special_chars, include_upper, include_lower, include_digits)

def main():
    mode = get_valid_input("Would you like to use advanced mode? It allows you to edit the properties of the password. (yes/no or y/n): ")
    
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the length.")

    if mode:
        # Advanced mode
        special_chars = get_special_characters()
        include_upper, include_lower, include_digits = get_inclusion_options()
        password = generate_password(length, special_chars, include_upper, include_lower, include_digits)
    else:
        # Basic mode
        password = generate_basic_password(length)
    
    print(f"Generated password: {password}")
    
    # Copy the password to the clipboard
    pyperclip.copy(password)
    print("Password has been copied to your clipboard.")

if __name__ == "__main__":
    main()

