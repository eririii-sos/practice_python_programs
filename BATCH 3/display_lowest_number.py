# Initialize a variable to track the lowest number
lowest_number = None

while True:
    try: 
        user_input = int(input("Enter a number: ")) # Get user input
        
        # Update the lowest number every input
        if lowest_number is None or user_input < lowest_number:
            lowest_number = user_input
    
    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break

# Display lowest number input