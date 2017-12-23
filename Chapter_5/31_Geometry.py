import math
r = input("Enter the length from the center to a vertex:")

s = (2 * r) * math.sin(math.pi / 5)
Area = ((3 * math.sqrt(3))/2) * (s ** 2)

print("The area of the pentagon is",Area)