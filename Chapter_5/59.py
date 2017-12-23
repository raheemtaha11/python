year = 0 # year 0
tuition = 10000 # Year 1

while year < 4:
	year += 1
	tuition *= 0.05

print("Tuition will be $" + format(tuition, ".2f"), "in", year,"years")