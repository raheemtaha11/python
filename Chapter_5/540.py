import random

random.randint(0,1)
both =random.randint(0,1)
heads = 0
tails = 0
for x in range(1,1000000):
	heads += 1
	tails += 1
	print("heads -",heads,\
		  "tails -", tails)
  