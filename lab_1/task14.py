N = int(input("What`s N?"))

# using while loop


def fib_iterative(n):
    i = 2
    f = [0, 1]
    while i <= n:
        f.append(f[i-1] + f[i-2])
        i += 1
    print(f)


fib_iterative(N)


# using for loop

def fib_iterative2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return print(f)


fib_iterative2(N)

# using recursion


def fib_recursive(n, f=[0, 1]):
    if n == 0:
        return [0]
    elif n == 1:
        return f
    else:
        f.append(f[-1] + f[-2])
        return fib_recursive(n-1, f)


result = fib_recursive(N)
print(result)
