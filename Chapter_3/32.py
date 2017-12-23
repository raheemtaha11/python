import math

x1,y1 = input("Enter point 1 (latitude and longiude) in degrees:")
x2,y2 = input("Enter point 2 (latitude and longiude) in degrees:")

d = 6371.01 * math.acos(math.sin(math.radians(x1))) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)
print("The distance between the two points is",d,"km")