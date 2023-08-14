N = int(input("Enter what should be the sum of the numbers: "))
numbers = []
i = 0

# loop for gradual input
while i < N:
    n = int(input("What`s n? "))
    # add number to the list
    numbers.append(n)
    i = i + 1
    print(i)
print(numbers)
