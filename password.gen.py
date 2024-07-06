import random
import string
import pyperclip

def genpass(length, special_chars='', upper=True, lower=True, digits=True):
    characters = ''
    
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    
    if special_chars:
        characters += special_chars
    
    if not characters:
        print("no characters to choose from for password generation.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def special_ch():
    special_chars = string.punctuation
    print(f"available special characters: {special_chars}")
    selected_chars = input("enter the special characters you want to include (e.g., @#$%&*), or press enter to include all: ").strip()
    
    if not selected_chars:
        return special_chars
    
    invalid_chars = [char for char in selected_chars if char not in special_chars]
    if invalid_chars:
        print(f"warning: the following characters are not in the standard special characters set and will be ignored: {''.join(invalid_chars)}")
        selected_chars = ''.join([char for char in selected_chars if char in special_chars])
    
    return selected_chars

def inputcheck(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        else:
            print("invalid response. please enter 'yes', 'no', 'y', or 'n'.")

def included():
    upper = inputcheck("include uppercase letters? (y/n): ")
    lower = inputcheck("include lowercase letters? (y/n): ")
    digits = inputcheck("include digits? (y/n): ")
    return upper, lower, digits

def easypass(length):
    special_chars = string.punctuation
    upper = True
    lower = True
    digits = True
    return genpass(length, special_chars, upper, lower, digits)

def main():
    mode = inputcheck("would you like to use advanced mode? it allows you to edit the properties of the password. (y/n): ")
    
    while True:
        try:
            length = int(input("enter the length of the password: "))
            if length <= 0:
                print("length must be a positive integer. please try again.")
                continue
            break
        except ValueError:
            print("invalid input. please enter a valid integer for the length.")

    if mode:
        special_chars = special_ch()
        upper, lower, digits = included()
        password = genpass(length, special_chars, upper, lower, digits)
    else:
        password = easypass(length)
    
    print(f"generated password: {password}")
    
    pyperclip.copy(password)
    print("password has been copied.")



if __name__ == "__main__":
    main()

