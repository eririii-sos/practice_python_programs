# Display what is being asked from the user
print("Enter 10 numbers:")

# Empty list to store the 10 number input
numbers = [] 

# Collect user input then insert them inside empty list
for i in range(1, 11):
    num = int(input(f"{i}: "))
    numbers.append(num)

# Identifying odd numbers
print("Odd numbers:")
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        print(num)