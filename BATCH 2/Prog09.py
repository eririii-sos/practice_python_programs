# Print all numbers from 0 to 100 except those ending in zero and five
print("All numbers from 0 to 100 not ending with zero or five:")
for num in range(101):
    if num % 10 != 0 and num % 5 != 0: 
        print(num)