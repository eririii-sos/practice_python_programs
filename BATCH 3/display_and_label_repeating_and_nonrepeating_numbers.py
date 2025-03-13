# Initialize empty list to store every input
input_numbers = []

# Get user input
while True:
    try:
        user_input = int(input("Enter a number: "))
    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break
    
# Check if input is new or a duplicate
    if user_input in input_numbers:
        print("Duplicate")
    else:
        print("Unique") # If not a duplicate, add the new/unique number to the list  