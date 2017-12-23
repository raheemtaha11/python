M=input("Enter the amount of water in kilograms:")
initialTemperature=input("Enter the initial temperature:")
finalTemperature=input("Enter the final temperature:")
E=M * (finalTemperature - initialTemperature) * 4184
print("The energy needed is",E)