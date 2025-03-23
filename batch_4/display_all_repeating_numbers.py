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
duplicate_numbers = []
for number_set in all_input:
    if all_input.count(number_set) > 1 and number_set not in duplicate_numbers:
        duplicate_numbers.append(number_set)

# Display output
if duplicate_numbers:
    print(f"Numbers with duplicates: {duplicate_numbers}")
else:
    print("No duplicates found.")