def func(N):
    for i in range(1, N +1):
        for j in range(1, N +1):
            print(i * j, end=' ')
        print()


n = int(input("What`s N "))
func(n)
