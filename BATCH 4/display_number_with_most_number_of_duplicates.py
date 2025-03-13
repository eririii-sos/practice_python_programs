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
    most_repeating_number = max(set(number_set), key=number_set.count)
    count = number_set.count(most_repeating_number)
    print(f"The number with the most duplicates is {most_repeating_number} (appears {count} times).") # Display number with the most duplicates

else:
    print("No valid numbers were entered.") # In case where no numbers were entered