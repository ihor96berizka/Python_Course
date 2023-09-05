N = input('What`s your list? ').split()

# use slicing
if len(N) >= 3:
    print(N[slice(2,None,3)])
else:
    print('The list is too short.')

# use while loop

i = 2

while i <= len(N):
    if len(N) < 3:
        print('The list is too short.')
        break
    print(N[i], end=', ')
    i += 3

print()

# use for loop

offset = 0

for offset in range(2, len(N), 3):
    print(N[offset], end=', ')
if len(N) < 3:
    print('The list is too short.')