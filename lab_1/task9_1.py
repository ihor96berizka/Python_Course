def multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(i*j, end=' ')
            j += 1
        print()

        i += 1


n = int(input("What`s N "))
multiplication_table(n)
