# An example of a program that lets the user enter a year and then determines whether it is a leap year.

year = eval(input("Enter a year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
(year % 400 ==0)

# Display the result
print("year", "is a leap year?", isLeapYear)
