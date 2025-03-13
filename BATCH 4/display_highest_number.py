# Initialize a variable to track the highest number
highest_number = None

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input

        if highest_number is None or user_input > highest_number: # Update the highest number every input
            highest_number = user_input

# Error handling for invalid input
# Display highest number input