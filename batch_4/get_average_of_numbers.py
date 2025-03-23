# Initialize variables for total sum and count of numbers
total_sum = 0
count = 0

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input
        total_sum += user_input # Add to the total sum
        count += 1 # Increment the count

    except ValueError: # Error handling for invalid input
        print("Invalid input! Terminating the program.")
        break
    
# Calculate and display the average if numbers were entered
if count > 0:
    average = total_sum / count
    print(f"The average is: {average}")
    
else:
    print("No valid numbers entered.")