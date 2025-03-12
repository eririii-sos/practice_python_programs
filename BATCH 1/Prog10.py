# Print all numbers from 0 to 100 except those ending in zero
for num in range(101):
    if num % 10 != 0: 
        print(num)