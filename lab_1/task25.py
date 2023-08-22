magic_number = 737

while True:
    N = int(input("What`s N?"))

    if N != magic_number:
        print("Oops, you did not guess the magic number")

    else:
        print("Wow, you guessed the magic number. Now you will earn a lot of dollars")
        break