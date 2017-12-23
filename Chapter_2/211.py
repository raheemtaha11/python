finalAccountValue = input("Enter final account value:")
annualInterestRate = input("Enter annual interest rate:")
numberOfYears = input("Enter number of years:")

initialDepositAmount = finalAccountValue / ((( annualInterestRate/100) / 12) ** (numberOfYears * 12) / 12)

print("Initial deposit value is",initialDepositAmount + 1)