magic_number = 737

N = int(input("What`s N?"))

while N != magic_number:
    print("Oops, you did not guess the magic number")
    break
else:
    print("Wow, you guessed the magic number. Now you will earn a lot of dollars")