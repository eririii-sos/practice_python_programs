# User input
print("Enter 10 numbers")
for i in range(10):
    while True:
        try:

            number_input = int(input(f"Input {i+1}: "))
            break
        # Restriction so user only types numbers
        except ValueError:
            print("Invalid input! Please enter a number.")
            
# Display output