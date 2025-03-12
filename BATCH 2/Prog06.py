# Collecting user input for 10 numbers
print("Enter 10 numbers:")
numbers = [] 

for i in range(1, 11):
    num = int(input(f"{i}: "))
    numbers.append(num)

# Perform the subtraction (first number minus all of the remaining numbers)
first_number = numbers[0]

print(f"Difference of {first_number} and the remaining numbers:")
for num in numbers[1:]:
    result = first_number - num
    print(f"{first_number} - {num} = {result}")