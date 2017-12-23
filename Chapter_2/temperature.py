import math
T=input("Enter the temperature in Fahrenheit between -58 and 41:")
W=("Enter the wind speed in miles per hour above 2 miles per hour:")
chill = ((35.74 + 0.6215*T) - (35.75 * W ** 0.16) + (0.4275 * T) * (W * 0.16))

print("The wind chill index is",chill )

if T < -58\
or T > 41\
or W < 2:\
	print("invalid input")