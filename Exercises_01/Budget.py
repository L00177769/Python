# Script: Budget.py
# Author: Martina Atkinson L00177769
# Purpose: To calculate my budget for the semester
# Prerequisites: None
# Tested: 29/9/2012

# create and assign values to variables
income = 2600
# create a dictionary item for my expenses
expenditure = {'Rent':1500, 'Food':120, 'Clothing':60,  'Entertainment': 90,  'Miscelleanus Expenses':200}
# created total_expenditure to hold the values as integar type
total_expenditure = sum(expenditure.values())
print("Total Expenditure:€", total_expenditure)
savings = income - total_expenditure 

# created if/elif/else to print text specific to results

if savings  > 0:
 print(f"Well done you are saving:€{savings}")
elif savings < 0:
 print(f"You are in the red by €{savings} my friend")
else:
 print("Your are only breaking even, ")



