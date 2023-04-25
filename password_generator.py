import random
import string

def generate_password(length: int, use_punctuation: bool) -> str:
    """
    Generate a random password of the specified length by user, using a combination
    of letters, digits, and let user decide if punctuation should be added as well.

    Parameters:
    length (int): The length of the password to generate.
    use_punctuation (bool): Whether to include punctuation characters in password.

    Returns:
    str: A randomly generated password.

    Example:
    generate_password(8, True)
    Generated password: xQ63SO==
    """

    # Define possible characters that can be used in the password
    if use_punctuation:
        characters = string.ascii_letters + string.punctuation + string.digits
    else:
        characters = string.ascii_letters + string.digits

    # Generate password by randomly selecting characters from the character set
    password = "" 
    for idx in range(length):
        password += random.choice(characters)
    return password

def password_strength(password: str) -> str:
    """
    Determines whether generated password is a weak or strong password. It determines that by 
    looking whether the size of the password is less than six, or if all the characters in the 
    password is all numeric, or if all the characters is only lowercase or only uppercase.

    Parameters:
    password (str): The generated password

    Returns:
    str: The strength of the password that was generated.

    Example:
    Case 1:
    generate_password(8, True)
    Generated password: xQ63SO==
    Password strength: strong

    Case 2:
    generate_password(6, False)
    Generated password: 328193
    Password strength: weak
    """
    strength = ""
    if len(password) < 6:
        strength = "weak"
    elif password.isnumeric():
        strength = "weak"
    elif password.islower() or password.isupper():
        strength = "weak"
    else:
        strength = "strong"
    return strength

if __name__ == "__main__":
    # Prompt user for desired password length
    while True:
        try:
            length = int(input("Please enter desired password length: "))
            break
        except ValueError:
            print("Please enter an integer value.")

    # Prompt user for whether to include punctuation
    while True:
        response = input("Do you want to include punctuation? (y/n): ")
        if response.lower() == "y":
            use_punctuation = True
            break
        elif response.lower() == "n":
            use_punctuation = False
            break
        else:
            print("Please enter 'y' or 'n'.")

    # Generate password
    password = generate_password(length, use_punctuation)
    strength = password_strength(password)

    # Display generated password
    print(f'Generated password: {password}')
    print(f'Password strength: {strength}')