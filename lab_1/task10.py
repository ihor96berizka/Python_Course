def func(n):
    sum = 0
    for x in range(1, N+1):
        sum += x
    return sum


#getting number from user
N = int(input("What`s N?"))
sum = func(N)
print(sum)
