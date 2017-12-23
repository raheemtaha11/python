import random

rock =  2
paper = 3
scissors = 1

you = input("rock, paper, scissors:")
bro = random.randint(1,3)
x = 0
y = 0
z = 0
if you == bro:
    print("Draw")
    z += 1
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
while x <  2:
    you = input("rock, paper, scissors:")
    if x == 2 :
        break
        print("You win this round.")

continueLoop = 'Y'
while continueLoop == 'Y':
    you = input("rock, paper, scissors:")
    continueLoop = input("Enter Y if you want to continue playing and N if you don't:" )

while y < 2:
    you = input("rock, paper, scissors:")
    if y == 2:
        break
        print("You lose this round")

continueLoop = 'Y'
while continueLoop == 'Y':
    you = input("rock, paper, scissors:")
    continueLoop = input("Enter Y if you want to continue playing and N if you don't:" )
    
while z < 2:
     you = input("rock, paper, scissors")
     if z == 2:
         break
         print("This round is a draw")

continueLoop = 'Y'
while continueLoop == 'Y':
    you = input("rock, paper, scissors")
    continueLoop = input("Enter Y if you want to continue playing and N if you don't:")
