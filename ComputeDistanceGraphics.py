# Enter the first point with two float values
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))

# Enter the second point with two float values
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

# Computer the distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

print("The distance between the two points are", distance)
