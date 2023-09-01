List = input('What`s your list? ').split()

# use slicing
print(List[2])

# use while loop

i = 0

while True:
    i += 1
    if i == 2:
        print(List[i])
        break

# use for loop

offset = 0

for item in List:
    if offset == 2:
        print(item)
    offset += 1