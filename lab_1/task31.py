import random
N = int(input('What`s number? '))

with open('numbers.txt', 'w') as file:
    i = 0
    while i < N:
        random_number = random.randint(1, 100)
        file.write(f'{random_number}\n')
        i += 1
