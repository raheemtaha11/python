import random

rock =  2
paper = 3
scissors = 1

you = input("rock,paper,scissors:")
bro = random.randint(1,3)
if you == bro:
    print("Draw")
if (you == rock) and (bro == paper):
    print("You are rock, the Computer is paper.")
    print("You lose")
if (you == paper) and (bro == rock):
    print("You are paper, the Computer is rock.")
    print("You win")
if (you == paper) and (bro == scissors):
    print("You are paper, the Computer is scissors.")
    print("You lose")
if (you == scissors) and (bro == paper):
    print("You are scissors, the Computer is paper.")
    print("You win")
if (you == scissors) and (bro ==rock):
    print("You are scissors, the Computer is rock.")
    print("You lose")
if (you == rock) and (bro == scissors):
    print("You are rock, the Computer is scissors.")
    print("You win")         