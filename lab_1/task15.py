import math


def func(x):
    f = 0.5*x**3 + 0.5*x**2 - 1
    return f


# ihm -  interval halving method


def ihm(a, b, eps):
    c = (b + a) / 2
    f_c = func(c)
    f_a = func(a)
    f_b = func(b)
    if math.isclose(f_c, 0, rel_tol=eps, abs_tol=eps):
        return round(c)
    elif f_a * f_c < 0:
        return ihm(a, c, eps)
    else:
        return ihm(b, c, eps)


def main():
    eps = 1e-4
    a = -5
    b = 5
    result = ihm(a, b, eps)
    print(result)


main()
