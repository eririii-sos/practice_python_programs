# Get user input
try:
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: " ))
    
    # Get the remainder of numbers
    try:
        numbers_remainder = first_number % second_number
        print(f"The remainder of {first_number} and {second_number} is {numbers_remainder}") # Display output

    except ZeroDivisionError: # Division by zero handling
        print("Error: Division by zero is not allowed. Terminating the program.")