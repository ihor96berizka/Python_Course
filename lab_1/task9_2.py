def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end=' ')
        print()


n = int(input("What`s N "))
multiplication_table(n)
