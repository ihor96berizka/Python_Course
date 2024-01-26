N = int(input("What`s N?"))

# using while loop


def fib_iterative(n):
    i = 2
    F = [0,1]
    while i <= n:
        F.append(F[i-1] + F[i-2])
        i += 1
    print(F)


fib_iterative(N)


# using for loop

def fib_iterative2(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return print(F)


fib_iterative2(N)

# using recursion


def fib_recursive(n):


