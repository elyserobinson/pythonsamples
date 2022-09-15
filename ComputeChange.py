# This program allows the user to enter an amount as a floating point value representing a total in dollars and centsand then outputs a report listing the monetary equivalent in dollars, quarters, dimes, nickels, and pennies.


# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56:"))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount =remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of dimes in the remaining amount
numberOfNickles = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of\n",\
"\t", numberOfOneDollars, "dollars\n",\
"\t", numberOfQuarters, "quarters\n",\
"\t", numberOfDimes, "dimes\n",\
"\t", numberOfNickles, "nickels\n",\
"\t", numberOfPennies, "pennies")
