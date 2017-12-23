import math

x1,y1 = input("Enter point 1 (latitude and longiude) in degrees:")
x2,y2 = input("Enter point 2 (latitude and longiude) in degrees:")

d = 6371.01 * accos(sin(math.radians(x1))) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2)
print("The distance between the two points is",d)