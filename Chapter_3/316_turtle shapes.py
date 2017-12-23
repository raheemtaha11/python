import turtle

radius=input("Enter radius:")

turtle.pensize(3) # Set pen thickness to 3 pixels

turtle.penup
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(radius, steps = 3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("orange")
turtle.circle(radius, steps = 4)
turtle.end_fill

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(radius,steps=5)
turtle.end_fill()

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(radius,steps= 6)
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("orange")
turtle.circle(radius,steps = 8)
turtle.end_fill()
turtle.color("orange")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.write("Cool Colorful Shapes",font = ("Times",18,"bold"))
turtle.hideturtle()

turtle.done()

