import turtle

semi = 0
round = 0
place = 1
area = 0
while semi < 10:
	turtle.penup()
	turtle.goto(place, area)
	turtle.pendown()
	turtle.circle(round)
	round += 20
	area += -20
	semi += 1

turtle.done()