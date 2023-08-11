N = int(input("Enter what should be the sum of the numbers: "))
numbers = []
i = 0

#loop for gradual input
while True:
    n = int(input(f"What number is {i+1}? "))
    #add number to the list
    numbers.append(n)
    i += 1
    if len(numbers) < N:
        continue
    else:
        break

print(numbers)