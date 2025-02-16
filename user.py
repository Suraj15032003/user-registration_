import re

def valid_first_name():
    """
    Validates the first name.
    
    - The name must start with an uppercase letter.
    - The remaining letters should be lowercase.
    - Minimum length: 2 characters.

    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-z]{1,}$"
        first_name = input("Enter first name: ").strip()

        if not first_name:
            raise ValueError("First name cannot be empty.")

        if re.match(pattern, first_name):
            print("Valid first name.")
        else:
            print("Invalid first name. It should start with an uppercase letter and have at least 2 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_last_name():
    """
    Validates the last name.
    
    - The last name must start with an uppercase letter.
    - Must be at least 3 characters long.

    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-z]{2,}$"
        last_name = input("Enter your last name: ").strip()

        if not last_name:
            raise ValueError("Last name cannot be empty.")

        if re.match(pattern, last_name):
            print("Valid last name.")
        else:
            print("Invalid last name. It should start with an uppercase letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_email():
    """
    Validates an email address.

    - Must contain alphanumeric characters before @.
    - Can have an optional dot before @.
    - Must have a domain after @ with at least 2 letters.
    - Can have an optional subdomain.

    Returns:
        None
    """
    try:
        pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
        email = input("Enter your email: ").strip()

        if not email:
            raise ValueError("Email cannot be empty.")

        if re.match(pattern, email):
            print("Valid email.")
        else:
            print("Invalid email format. Please enter a valid email (e.g., example@gmail.com).")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_mobile_number():
    """
    Validates an Indian mobile number.

    - Must start with '91'.
    - Must have 10 digits starting with 6-9.

    Returns:
        None
    """
    try:
        pattern = r"^(91)[6-9][0-9]{9}$"
        mobile_number = input("Enter your phone number (with country code 91): ").strip()

        if not mobile_number:
            raise ValueError("Mobile number cannot be empty.")

        if re.match(pattern, mobile_number):
            print("Valid mobile number.")
        else:
            print("Invalid mobile number. It must start with '91' and have 10 digits after it.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def validate_password():
    """
    Validates if a password meets minimum length criteria.
    
    - Must be at least 8 characters long.

    Returns:
        None
    """
    try:
        password = input("Enter your password: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        pattern = r"^.{8,}$"
        if re.match(pattern, password):
            print("Valid password.")
        else:
            print("Invalid password. It must be at least 8 characters long.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def password_uppercase():
    """
    Checks if a password contains at least one uppercase letter.

    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.

    Returns:
        None
    """
    try:
        password = input("Enter a password for uppercase validation: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        pattern = r"^(?=.*[A-Z]).{8,}$"

        if re.match(pattern, password):
            print("Password is valid (contains at least one uppercase letter).")
        else:
            print("Invalid password. It must have at least one uppercase letter.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to execute all validation functions.
    """
    try:
        valid_first_name()
        valid_last_name()
        valid_email()
        valid_mobile_number()
        validate_password()
        password_uppercase()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
