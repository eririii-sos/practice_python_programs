# Initialize an empty list to store the numbers
number_set = []

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input
        number_set.append(user_input) # Add new input to the list

    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break

# Sort the list of numbers in ascending order
number_set.sort()

# Display the numbers in ascending order
print(f"Numbers from lowest to highest: {number_set}")