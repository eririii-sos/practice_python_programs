# Print all numbers from 0 to 100 except those ending in zero and five
for num in range(101):
    if num % 10 != 0 and num % 5 != 0: 
        print(num)