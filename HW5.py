# Find the greatest common divisor of two integers.

n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

d = 2
gcd = 1

while d <= n1 and d <= n2:
    if n1 % d == 0 and n2 % d == 0:
        for i in range(0, d-1):
            if n1 % (d - i) == 0 and n2 % (d - i) == 0:
                gcd = d
                break
            
    d += 1
    
print("The greatest common divisor for", n1, "and", n2, "is", gcd)




# A program that displays the PI value for i = 10,000, 20,000, .... and 100,000.

sum = 0

for i in range(10000, 11000, +10000):
    for k in range(1, i + 1):
        sum += ((-1) ** (k + 1)) / (2 * k - 1)
    PI = 4 * sum
    print("i =", i, ", ", "PI is =", PI)
 

# A program that displays the calendar for each month in the year.

month, year = eval(input("Enter a month (1-12) and a year (1900-3000): "))

if month == 1:
	print("January", year, "has 31 days.")
elif month == 2:
	# Check if the year is a leap year
	isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	if isLeapYear:
		print("February", year, "has 29 days.")
	else:
		print("February", year, "has 28 days.")
elif month == 3:
	print("March", year, "has 31 days.")
elif month == 4:
	print("April", year, "has 30 days.")
elif month == 5:
	print("May", year, "has 31 days.")
elif month == 6:
	print("June", year, "has 30 days.")
elif month == 7:
	print("July", year, "has 31 days.")
elif month == 8:
	print("August", year, "has 31 days.")
elif month == 9:
	print("September", year, "has 30 days.")
elif month == 10:
	print("October", year, "has 31 days.")
elif month == 11:
	print("November", year, "has 30 days.")
elif month == 12:
	print("December", year, "has 31 days.")
