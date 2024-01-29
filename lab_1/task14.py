# using while loop


def fib_iterative(n):
    i = 2
    f = [0, 1]
    while i <= n:
        f.append(f[i-1] + f[i-2])
        i += 1
    return f

# using for loop


def fib_iterative2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f

# using recursion


def fib_recursive(n, f=[0, 1]):
    if n == 0:
        return [0]
    elif n == 1:
        return f
    else:
        f.append(f[-1] + f[-2])
        return fib_recursive(n-1, f)

# main function


def main():
    n = int(input("What`s N?"))
    result1 = fib_iterative(n)
    result2 = fib_iterative2(n)
    result3 = fib_recursive(n)
    print(result1, result2, result3, sep='\n')


main()
