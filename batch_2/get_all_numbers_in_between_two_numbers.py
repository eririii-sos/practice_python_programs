# Initialized empty list to store input
mid_numbers = []

# Get user input
first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second Number: "))

# Find numbers in between given numbers
if first_number < second_number:
    for number in range(first_number + 1, second_number):
        mid_numbers.append(number)
    print(f"The number(s) in between {first_number} and {second_number} is/are: {mid_numbers}.")

else:
    for number in range(second_number + 1, first_number):
        mid_numbers.append(number)
    print(f"The number(s) in between {second_number} and {first_number} is/are: {mid_numbers}.")