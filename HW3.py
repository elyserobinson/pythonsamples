# A program that receives an ASCII code between 0 and 127 and displays its characters.

ascii = eval(input("Enter a number between 0 and 127: "))
code = chr(ascii)

print("The character is ", code)




# Write a program that reads the following information and prints a payroll statement:
  # vEmployee’s name (e.g., Smith)
  # Number of hours worked in a week (e.g., 10)
  # Hourly pay rate (e.g., 9.75)
  # Federal tax withholding rate (e.g., 20%)
  # State tax withholding rate (e.g., 9%) 

# Get the employee's name
name = input("Enter employee's name: ")
# Get the number of hours worked in a week
hours = eval(input("Enter number of hours worked in a week: "))
# Get the hourly pay rate
payRate = eval(input("Enter hourly pay rate: "))
# Get the federal tax withholding rate
fedTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))
# Get the state tax withholding rate
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))

# Calculate the gross Pay
grossPay = hours * payRate
# Calculate the federal withholding
fedTaxWithholding = grossPay * fedTaxWithholdingRate
# Calculate the state Withholding
stateTaxWithholding = grossPay * stateTaxWithholdingRate
# Calculate the total deduction totalDeduction = fedTaxWithholding + stateTaxWithholding
totalDeduction = fedTaxWithholding + stateTaxWithholding
# Calculate the net pay netPay = grossPay - totalDeduction
netPay = grossPay - totalDeduction

# Store, prepare and format the output into a string
out = "Employee Name: " + name + "\n\n"
out += "Hours Worked:  " + str(hours) + '\n'
out += "Pay Rate: $" + str(payRate) + '\n'
out += "Gross Pay: $" + str(grossPay) + '\n'
out += "Deductions:\n"
out += "  Federal Withholding (" + str(fedTaxWithholdingRate * 100) + "%): $" + str(int(fedTaxWithholding * 100) / 100.0) + '\n'
out += "  State Withholding (" + str(stateTaxWithholdingRate * 100) + "%):"  + "  $" + str(int(stateTaxWithholding * 100) / 100.0) + '\n'
out += "  Total Deduction:" + "  $" + str(int(totalDeduction * 100) / 100.0) + '\n'
out += "Net Pay:" + "   $" + str(int(netPay * 100) / 100.0)

# Display the result
print(out)




# Write a program that prompts the user to enter the three points p1, p2, p3 for a triangle and display its angles.

import turtle
import math

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1 (" + "{0:0.2f}".format(A) + ")")
turtle.goto(x2, y2)
turtle.write("p2 (" + "{0:0.2f}".format(B) + ")")
turtle.goto(x3, y3)
turtle.write("p3 (" + "{0:0.2f}".format(C) + ")")
turtle.goto(x1, y1)

turtle.hideturtle()

turtle.done()

