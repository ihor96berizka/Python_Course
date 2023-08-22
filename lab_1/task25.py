magic_number = 737

N = int(input("What`s N?"))

while True:
    if N != magic_number:
        print("Oops, you did not guess the magic number")
        N = int(input("What`s N?"))
    else:
        print("Wow, you guessed the magic number. Now you will earn a lot of dollars")
        break