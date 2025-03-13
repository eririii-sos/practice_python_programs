# Initialize variables for total sum and count of numbers
total_sum = 0
count = 0

while True:
    try:
        user_input = int(input("Enter a number: ")) # Get user input
        total_sum += user_input # Add to the total sum
        count += 1 # Increment the count
    
# Calculate and display the average if numbers were entered