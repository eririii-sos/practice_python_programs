# Collecting user input for 10 numbers
print("Enter 10 numbers:")
numbers = [int(input(f"{i + 1}: ")) for i in range(10)] # List for collecting all inputs

# Start with the first number
difference = numbers[0]

# Perform subtraction of numbers
print(f"\nSubtracting the numbers:")
for num in numbers[1:]:
    print(f"{difference} - {num} = ", end="")
    difference -= num # Subtract current number from result
    print(difference) # Display result after every subtraction