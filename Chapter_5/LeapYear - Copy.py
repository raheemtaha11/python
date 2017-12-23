year = 2001
# Check if the year is a leap year
while year < 2100:
	isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	print(isLeapYear)