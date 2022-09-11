# Enter a number between 0 and 1000
num = int(input("Enter a number between 0 and 1000: "))

# Add up the numbers
x = num // 1000
x1 = (num - x * 1000) // 100
x2 = (num - x * 1000 - x1 * 100) // 10
x3 = num - x * 1000 - x1 * 100 - x2 * 10

# Display results
print("The sum of the digits are", x + x1 + x2 + x3)
