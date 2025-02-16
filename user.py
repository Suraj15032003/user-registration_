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
            print("It is a valid name.")
        else:
            print("It is an invalid name.")

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
            print("The last name is valid.")
        else:
            print("It is not a valid name.")

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
            print("Not a valid email.")

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
        mobile_number = input("Enter your phone number: ").strip()

        if not mobile_number:
            raise ValueError("Mobile number cannot be empty.")

        if re.match(pattern, mobile_number):
            print("Valid mobile number.")
        else:
            print("Not a valid number.")

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
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    main()