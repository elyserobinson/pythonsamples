# Enter a number between 0 and 1000
num = int(input("Enter a number between 0 and 1000: "))

# Add up the numbers
x = num // 1000
x1 = (num - x * 1000) // 100
x2 = (num - x * 1000 - x1 * 100) // 10
x3 = num - x * 1000 - x1 * 100 - x2 * 10

# Display results
print("The sum of the digits are", x + x1 + x2 + x3)






# Enter the first point with two float values
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))

# Enter the second point with two float values
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

# Enter the third point with two float values
x3, y3 = eval(input("Enter x2 and y2 for Point 3: "))

# Computer the area of the triangle
side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
side3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = round((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5, 2)

print("The area of the triangle is", round(area, 2))
