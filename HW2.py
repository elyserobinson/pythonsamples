'''
   CIST 005A Fall 2022
   HW Week 2 Chapter 2 Problem 2.1
   Description: Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result.
   Input: any number
   Output: Fahrenheit
   Student: Elyse Y. Robinson
   Known bugs: none.
   Date: September 6, 2022
'''

# Prompt the user to enter a number
celsius = eval(input("Enter any number for celsius: "))

# The formula to convert celsius to fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Display fahrenheit
print(celsius, "degrees celsius is", fahrenheit, "degrees fahrenheit.")

'''
Enter any number for celsius: 
0
0 degrees celsius is 32.0 degrees fahrenheit.
'''

print('')

'''
   CIST 005A Fall 2022
   HW Week 2 Chapter 2 Problem 2.6
   Description: Write a program that reads an integer between 0 and 1000 and adds all the digits in the integer.
   Input: A number between 0 and 1000
   Output: Adding of all numbers from the input
   Student: Elyse Y. Robinson
   Known bugs: none.
   Date: September 6, 2022
'''

# Enter a number between 0 and 1000
num = int(input("Enter a number between 0 and 1000: "))

# Add up the numbers
x = num // 1000
x1 = (num - x * 1000) // 100
x2 = (num - x * 1000 - x1 * 100) // 10
x3 = num - x * 1000 - x1 * 100 - x2 * 10

# Display results
print("The sum of the digits are", x + x1 + x2 + x3)


'''
Enter a number between 0 and 1000: 
333
The sum of the digits are 9
'''

print('')

'''
   CIST 005A Fall 2022
   HW Week 2 Chapter 2 Problem 2.14
   Description: Write a program that prompts the user to enter the three points of a triangle and displays its area.
   Input: 3 points
   Output: Area of a triangle
   Student: Elyse Y. Robinson
   Known bugs: none.
   Date: September 6, 2022
'''

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

'''
Enter x1 and y1 for Point 1: 
1.5, -3.4
Enter x2 and y2 for Point 2: 
4.6, 5
Enter x2 and y2 for Point 3: 
9.5, -3.4
The area of the triangle is 33.6
'''
