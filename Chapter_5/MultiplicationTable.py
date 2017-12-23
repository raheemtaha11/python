print("        Multiplication Table")
# Display the number title
print("  |")
for j in range(1,10):
	print(" ", j)
print() # Jump to the new line
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

# Display table body
for i in range(1,10):
		print(i, "|")
		for j in range(1,10):
			# Display the product and align properly
			print(format(i * j, "4d"))
		print() # Jump to  the new line
