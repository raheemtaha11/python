temperatureOutside=input("Enter the temperature in Fahrenheit between -58 and 41:")
if temperatureOutside < -58\
or temperatureOutside > 41:
   print("invalid input")
windSpeed = input("Enter the wind speed in miles per hour above 2 miles per hour:")
windChill  = (35.74 + 0.6215 * temperatureOutside - 35.75 * (windSpeed ** 0.16) + 0.4275 * temperatureOutside * (windSpeed * 0.16))
if temperatureOutside < -58\
or temperatureOutside > 41\
or windSpeed < 2:
	print("invalid input")
else:
	print("The wind chill index is",windChill )