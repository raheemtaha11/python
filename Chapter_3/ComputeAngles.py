import turtle
import math

x1,y1,x2,y2,x3,y3 = input("Enter six points :")

a = math.sqrt((x2-x3) * (x2-x3) + (y2-y3) * (y2-y3))
b = math.sqrt((x1-x3) * (x1-x3) + (y1-y3) * (y1-y3))
c = math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are ",round(A * 100) / 100.0, round(B * 100) / 100.0, round(C*100)/100.0)
 
angle_1 = round(A * 100) / 100.0
angle_2 = round(B * 100) / 100.0
angle_3 = round(C*100)/100.0

turtle.penup()
turtle.goto(0, -50)	
turtle.pendown()
turtle.goto(x1,x2) 
turtle.write(angle_1)
turtle.goto(x2,x1)
turtle.write(angle_2)
turtle.goto(x3,x2)
turtle.write(angle_3)
turtle.hideturtle()
turtle.done()