import math


def a_quadratic_equation(a, b, c, Eps):
    D = b**2 - 4 * a * c
    if math.isclose(D,0, rel_tol=Eps, abs_tol=Eps):
        x = round((-b / 2 * a), 2)
        return ((x))
    elif D > 0:
        x1 = round(-b + math.sqrt(D) / (2 * a), 2)
        x2 = round(-b - math.sqrt(D) / (2 * a), 2)
        return ((x1, x2))
    else:
        return (())


print("Hello, you are greeted by a program that solves a quadratic equation")

#assigning a variable to to represent a specific value of precision
eps = 0.001

#receive data from the user
A = float(input("Enter the coefficient a: "))
B = float(input("Enter the coefficient b: "))
C = float(input("Enter the coefficient c: "))

result = a_quadratic_equation(A, B, C, eps)
print(result)
