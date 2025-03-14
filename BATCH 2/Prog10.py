# Initialized empty list to store input
x = []

# Get user input
first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second Number: "))

# Find numbers in between given numbers
if n1 < n2:
    for num in range(n1 + 1, n2):
        x.append(num)

else:
    for num in range(n2 + 1, n1):
        x.append(num)

print(x)