# Initialize empty list to store every input
all_input = []

# Get user input
print("Enter 10 numbers")
for i in range(10):
    while True:
        try:
            number_input = int(input(f"{i+1}: "))
            all_input.append(number_input)  # Adds number entered to the list
            break
        except ValueError: # Error handling for invalid input
            print("Invalid input! Please enter a valid number.")
       
# Determine duplicates
# Display output