import time

alarm = input("Enter the number of seconds:")
time.sleep(alarm)
past = alarm - 1
while alarm > past:
	past += -1
	alarm -= 1
	print(past,"seconds remaining")
	if past == 0:
		break
		print("Stopped")	