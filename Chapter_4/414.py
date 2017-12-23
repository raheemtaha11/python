import random

random.randint(0,1)
guess= input("Choose,heads or tails(0 or 1)?")
both =random.randint(0,1)
if guess == both:
    print("you are correct !")
else:
    print("wrong")
  