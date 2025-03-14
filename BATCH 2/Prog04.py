# Get user input
try:
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: " ))
    
    # Calculate quotient of numbers without the decimal point
    try:
        numbers_quotient = first_number // second_number
        print(f"The quotient of {first_number} and {second_number} is {numbers_quotient}") # Display output
    
    except ZeroDivisionError: # Division by zero handling
        print("Error: Division by zero is not allowed. Terminating the program.")

