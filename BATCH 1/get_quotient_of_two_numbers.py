# User Input
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: " ))

# Calculate quotient of numbers
try:
     quotient = first_number / second_number
     print(f"The quotient of {first_number} and {second_number} is {quotient}")
   
except ZeroDivisionError: # Division by zero handling
    print("Error: Division by zero is not allowed. Terminating the program.")