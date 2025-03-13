# Initialize empty list to store every input
number_set = []

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input
        number_set.append(user_input)
    
    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break

# Find number with the most duplicates
if number_set:

    number_count = {user_input: number_set.count(user_input) for user_input in set(number_set)} # Counting frequencies of all numbers
    max_count = max(number_count.values()) # Find highest count of duplicates
    most_repeating_number = [user_input for user_input, count in number_count.items() if count == max_count] # Find all numbers that have highest number of duplicates
    print(f"The number(s) with the most duplicates is/are {most_repeating_number} (appears {max_count} times).") # Display number(s) with the most duplicates

else:
    print("No valid numbers were entered.") # In case where no numbers were entered