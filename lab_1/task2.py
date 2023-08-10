import math
print("Hello, you are greeted by a program that solves a quadratic equation")

#assigning a variable to to represent a specific value of precision
Eps = 0.001

#receive data from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

#find the discriminant
D = b**2 - 4 * a * c

#determination of the solution for the discriminant which is equal to 0 and is approximate
if math.isclose(D,0, rel_tol=Eps, abs_tol=Eps):
    x = -b / 2 * a
    print("x =", round(x, 2))
#the standard solution for the discriminant is greater than 0
elif D > 0:
    x1 = (-b + math.sqrt(D) / (2 * a))
    x2 = (-b - math.sqrt(D) / (2 * a))
    print("x1 =", round(x1, 2))
    print("x2 =", round(x2, 2))
else:
    print("Real solutions are not possible, because the discriminant is negative.")
