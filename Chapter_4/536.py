import random

rock =  2
paper = 3
scissors = 1

you = input("rock, paper, scissors:")
bro = random.randint(1,3)
x = 0
y = 0


if you == bro:
    print("Draw")
    
if (you == rock) and (bro == paper):
    print("You are rock, the Computer is paper.")
    print("You lose")
    y += 1
if (you == paper) and (bro == rock):
    print("You are paper, the Computer is rock.")
    print("You win")
    x += 1
if (you == paper) and (bro == scissors):
    print("You are paper, the Computer is scissors.")
    print("You lose")
    y += 1
if (you == scissors) and (bro == paper):
    print("You are scissors, the Computer is paper.")
    print("You win")
    x += 1
if (you == scissors) and (bro ==rock):
    print("You are scissors, the Computer is rock.")
    print("You lose")
    y += 1
if (you == rock) and (bro == scissors):
    print("You are rock, the Computer is scissors.")
    print("You win")
    x += 1