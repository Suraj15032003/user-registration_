import re

def valid_first_name():
    """
    Validates the first name.
    
    - Must start with an uppercase letter.
    - Remaining letters should be lowercase.
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

def main():
    """
    Main function to execute the name validation.
    """
    valid_first_name()

if __name__ == "__main__":
    main()
