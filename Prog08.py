# Collecting user input for 10 numbers
print("Enter 10 numbers:")
numbers = [] 

for i in range(1, 11):
    num = int(input(f"{i}: "))
    numbers.append(num)

# Identifying odd numbers
print("Odd numbers:")
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        print(num)