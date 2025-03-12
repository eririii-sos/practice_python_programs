# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# User Input
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second Number: "))

# 
x = []

# 
if n1 < n2:
    for num in range(n1 + 1, n2):
        x.append(num)

else:
    for num in range(n2 + 1, n1):
        x.append(num)

print(x)