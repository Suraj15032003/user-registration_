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
        pattern = "^[A-Z][a-z]{1,}$"
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

def valid_last_name(last_name):
    """
    Validates the last name.
    - The last name must start with an uppercase letter.
    - Must be at least 3 characters long.
    Args:
        last_name (str): The last name entered by the user.
    Returns:
        None
    """
    try:
        pattern = "^[A-Z][a-z]{2,}$"
        
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

def main():
    """
    Main function to execute name validation.
    """
    try:
        valid_first_name()
        
        last_name = input("Enter your last name: ").strip()
        valid_last_name(last_name)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()