# Welcome message
print("Welcome to my simple calculator!")

# Ask the user for a number
number = input("Enter a number: ")

try:
    # Convert to float and perform a calculation
    value = float(number)
    result = value * 5

    # Display result
    print(f"Your number multiplied by 5 is: {result}")

except ValueError:
    # Handle invalid input
    print("Please enter a valid number next time.")
