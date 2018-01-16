import math

a = int(input("Enter the coefficients of a:"))
b = int(input("Enter the coefficients of b:"))
c = int(input("Enter the coefficients of c:"))

d = b**2-4*a*c

if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b+d**0.5)/(2*a)
    print("This equation has one solutions: ", x)
else:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print("This equation has two solutions: ", x1, " and", x2)
