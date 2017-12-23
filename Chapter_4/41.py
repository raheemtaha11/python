import math

a,b,c = input("Enter a,b,c:")
r1 = -b + (math.sqrt(b**2 - (4 * a * c ))) / 2 * a
r2 = -b + (math.sqrt(b**2 - (4 * a * c))) / 2 * a
if b**2 - (4 * a * c) >= 0 :
	print("Roots are",r1, "and",r2)
if b**2 - (4 * a * c) == 0:
        print("the root is",r1)
else:
     print("The equation has no real roots")