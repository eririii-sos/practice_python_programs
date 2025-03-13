# Display what is being asked from the user
print("Enter 10 numbers:")

# Empty list to store every number input 
number_set = []

# Collect user input 
for i in range(1,11):
    while True:
        try:
            all_numbers = int(input(f"{i}: "))
            number_set.append(all_numbers)
            break
        except ValueError: # Error handling for invalid input
            print("Invalid input! Plese enter a valid number.")

# Identify all the non-repeating numbers
non_repeating_numbers = [all_numbers for all_numbers in number_set if all_numbers.count(all_numbers) == 1]

# Display all non-repeating numbers only
print("Non-repeating numbers:", *non_repeating_numbers)