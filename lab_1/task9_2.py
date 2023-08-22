i = 1
N = int(input("What`s N"))

for i in range(N):
    j = 1
    for j in range(N):
        print(i * j, end=' ')
        j += 1
    print()

    i += 1
