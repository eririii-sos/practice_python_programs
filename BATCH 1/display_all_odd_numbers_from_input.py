# Display what is being asked from the user
print("Enter 10 numbers:")

# Empty list to store the 10 number input
number_set = [] 

# Collect user input then insert them inside empty list
for i in range(1, 11):
    number_input = int(input(f"{i}: "))
    number_set.append(number_input)

# Determine odd numbers
print("Odd numbers:")
for number_input in number_set:
    if number_input % 2 != 0:  # Check if the number is odd
        print(number_input)
