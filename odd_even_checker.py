#python


import re

def is_valid_number(user_input):
    """
    Check if the input is a valid integer and contains no special characters.
    """
    # Check if the input contains any letters or special characters (besides numbers)
    if re.match(r'^[+-]?\d+$', user_input.strip()):
        return True
    else:
        return False


def check_even_or_odd():
    """
    Main function to continuously ask the user for input to determine if the number is even or odd.
    """
    print("Welcome to the Even or Odd Checker!")
    print("Instructions: Please enter a number to check if it's even or odd.")
    print("Type 'exit' to quit the program.")
    
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Thank you for using the Even or Odd Checker. Goodbye!")
            break
        
        # Strip spaces from input and check if it's valid
        user_input = user_input.strip()

        if not user_input:
            print("Input cannot be empty. Please enter a number.")
            continue
        
        if not is_valid_number(user_input):
            print(f"Invalid input: '{user_input}'. Please enter only numbers without any special characters or letters.")
            continue
        
        # Convert input to integer after validating
        try:
            number = int(user_input)
            
            # Check if the number is even or odd
            if number % 2 == 0:
                print(f"{number} is an even number.")
            else:
                print(f"{number} is an odd number.")
        
        except ValueError:
            print(f"Invalid input: '{user_input}'. Please enter a valid number.")

# Main entry point of the program
if __name__ == "__main__":
    check_even_or_odd()
