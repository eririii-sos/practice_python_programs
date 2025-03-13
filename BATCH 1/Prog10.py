# Top label for output
print("All numbers from 0-100 not ending with zero:")

# Print all numbers from 0 to 100 except those ending in zero
for number_set in range(101):
    if number_set % 10 != 0: 
        print(number_set)