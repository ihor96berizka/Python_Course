i = 1
N = int(input("What`s N"))

while i <= N:
    j = 1
    while j <= N:
        print(i*j, end=' ')
        j += 1
    print()

    i += 1
