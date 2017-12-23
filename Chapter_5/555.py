import turtle

turtle.speed(7)
# Draw 16 - by 16 board

turtle.color("black") 
x = -80
for y in range(-90, 90 + 1, 7):
	turtle.penup()
	turtle.goto(x, y) # Draw a horizontal line
	turtle.pendown()
	turtle.forward(160)


y = 80
turtle.right(90)
for x in range(-90, 90 + 1, 7):
	turtle.penup()
	turtle.goto(x, y) # Draw a vertical line
	turtle.pendown()
	turtle.forward(160)

turtle.done()