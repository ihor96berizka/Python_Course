import math


def a_quadratic_equation(a, b, c, eps):
    d = b**2 - 4 * a * c
    if math.isclose(d, 0, rel_tol=eps, abs_tol=eps):
        x = round((-b / 2 * a), 2)
        return x
    elif d > 0:
        x1 = round(-b + math.sqrt(d) / (2 * a), 2)
        x2 = round(-b - math.sqrt(d) / (2 * a), 2)
        return x1, x2
    else:
        return ()


print("Hello, you are greeted by a program that solves a quadratic equation")

# assigning a variable to represent a specific value of precision
Eps = 0.001

# receive data from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

result = a_quadratic_equation(a, b, c, Eps)
if not result:
    print("Real solutions are not possible, because the discriminant is negative.")
else:
    print(result)
