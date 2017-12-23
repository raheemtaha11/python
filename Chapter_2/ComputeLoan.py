# Enter annual interest rate as a percetage, e.g., 7.25
annualInterestRate = (input("Enter annual interest rate, e.g., 7.25:"))

monthlyInterestRate= annualInterestRate/1200

# Enter number of years
numberOfYears=(input("Enter number of years as an integer,e.g.,5:"))


# Enter loan amount
loanAmount = (input("Enter loan amount,e.g., 120000.95:"))

# Calculate payment
monthlyPayment= loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))

totalPayment= monthlyPayment* numberOfYears* 12

# Display results
print("The monthly payment is", int(monthlyPayment* 100)/100)
print("The total payment is",int(totalPayment*100)/100)
