# Simple Calculator Program
# This program asks the user for a number, converts it,
# performs a calculation, and prints the result.

print("Welcome to my simple calculator!")

# Ask the user for a number
number = input("Enter a number: ")

try:
    # Convert user input to a float
    value = float(number)

    # Basic calculation (example: multiply by 5)
    result = value * 5

    # Display the result clearly
    print(f"Your number multiplied by 5 is: {result}")

except ValueError:
    # Error message if the input can't be converted
    print("Please enter a valid number.")
