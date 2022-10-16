from Circle import Circle

def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius", circle1.radius, "is", circle1.getaArea())
    
    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())
    
    # Create a circle with radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius", circl3.radius, "is", circl3.getArea())
    
    # Modify circle radius
    circle2.radius = 100 # or circle2.setRadius(100)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())

main() # Call the main function
