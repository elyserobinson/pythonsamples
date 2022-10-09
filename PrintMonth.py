def printMonth(year, month):
    print(year, month)
    
def printMonthTitle(year, month):
    print("printMonthTitle")

def getMonthBody(year, month):
    print("getMonthBody")

def getMonthName(month):
    print("getMonthName")
    
def getStartDay(year, month):
    print("getStartDay")

def getTotalNumberOfDays(year, month):
    print("getTotalNumberOfDays")

def isLeapYear(year):
    print("isLeapYear")

def main():
    # Prompt the user to enter year and month
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input("Enter month as a number between 1 and 12: "))
    
    # Print calendar for the month of the year
    printMonth(year, month)

main() # Call the main function
