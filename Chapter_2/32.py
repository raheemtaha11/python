import math
p1,p2 = input("Enter point 1 and point 2 (latitude and longitude) in degrees:")
p3,p4 = input("Enter point 3 point 4 (latitude and longitude) in degrees:")
radius = 6371.01
d = radius * math.acos(math.sin(p1)) * math.sin(p2) + math.cos(p2) * math.cos(p3-p4)
print("The distance between the two points is",d)