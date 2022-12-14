'''
A program to compute personal income tax. The program prompts the user to enter the filing status and taxable income and then compute the tax.

Enter 0 for single filers, 1 for married filing jointly, 2 for married filing separately, and 3 for head of household.

The program computes the tax for the taxable income based on the filing status.

For each filing status there are six tax rates. Each rate is applied to a certain amount of taxable income. For example, of a taxable income of $400,000 for single filers, $8,350 is taxed at 10%, (33,950 – 8,350) at 15%, (82,250 – 33,950) at 25%, (171,550 – 82,250) at 28%, (372,950 – 171,550) at 33%, and (400,000 – 372,950) at 35%.
'''

import sys

# Prompt the user to enter filing status
status = eval(input(
  "(0-single filer, 1-married jointly,\n" + 
  "2-married separately, 3-head of household)\n" + 
  "Enter the filing status: "
))

# Prompt the user to enable taxable income
income = eval(input("Enter the taxable income: "))

# Compute tax
tax = 0

if status == 0: # Compute tax for single filers
  if income <= 8350:
    tax = income * 0.10
  elif income <= 33950:
    tax = 8350 * 0.10 + (income - 8350) * 0.15
  elif income <= 82250:
    tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
    (income - 33950) * 0.25
  elif income <= 171550:
    tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
    (82250 - 33950) * 0.25 + (income - 82250) * 0.28
  elif income <= 372950:
    tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
    (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
    (income - 171550) * 0.33
  else:
    tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
    (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
    (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
elif status == 1: # Compute tax for married file jointly
  print("Left as exercise")
elif status == 2: # Compute tax for married separately
  print("Left as exercise")
elif status == 3: # Compute tax for head of household
  print("Left as exercise")
else:
  print("Error: invalid status")
  sys.exit

# Display the result
print("Tax is", format(tax, ".2f"))
