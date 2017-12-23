import random

number1 = random.randint(0,99)
number2 = random.randint(0,99)

if number1 < number2:
    number1, number2 = number2, number1

answer = input("What is" + str(number1) + "*" + str(number2) + "?")
if number1 * number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.",number1,"*",number2,"is", number1 * number2, ".")
