def f(x):
    # f = 0.5*x**3 + 0.5*x**2 - 1
    f = (x - 0.955)**2
    return f


# ihm -  interval halving method


def ihm(a, b, eps):
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return round((a + b) / 2)


def main():
        eps = 1e-4
        a = -5
        b = 5
        result = ihm(a, b, eps)
        print(result)


main()
