# Initialize a variable to track the highest number
highest_number = None

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input

        if highest_number is None or user_input > highest_number: # Update the highest number every input
            highest_number = user_input
    
    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break

# Display highest number input
if highest_number is not None:
    print(f"The highest number entered was: {highest_number}")