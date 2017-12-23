number=input("Enter a number between 0 and 1000:")
a=number%10
digit=number//10
b=digit%10
binary=digit//10
c=binary%10
answer=a+b+c
print("The sum of the digits is",answer)