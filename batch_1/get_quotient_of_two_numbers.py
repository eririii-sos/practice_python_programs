# Get user input
try:
     first_number = int(input("Enter First Number: "))
     second_number = int(input("Enter Second Number: " ))
     
     # Calculate quotient of numbers
     if first_number == 0 and second_number == 0:
          print("Error: Undefined. Terminating the program.")  # Handle division by zero or undefined 0/0
     
     else:
          quotient = first_number / second_number
          print(f"The quotient of {first_number} and {second_number} is {quotient}")

except ValueError:  # Handle non-numeric input
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:  # Division by zero handling (if second number is 0)
    print("Error: Division by zero is not allowed. Terminating the program.")