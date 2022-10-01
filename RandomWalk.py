# A Turtle program that simulates a random walk in a lattice (e.g., like walking around a garden and turning to look at certain flowers) that starts from the center and ends at a point on the boundary.

import turtle
from random import randint

turtle.speed(1) # Set the turtle speed to slowest

# Draw 16 by 16 lattice
turtle.color("gray") # Color for lattice
x = -80
for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # Draw a horizontal line
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # Draw a vertical line
    turtle.pendown()
    turtle.forward(160)

turtle.pensize(3)
turtle.color("red")

turtle.penup()
turtle.color("red")

turtle.penup()
turtle.goto(0, 0) # Go to the center
turtle.pendown()

x = y = 0 # Current pen location at the center of lattice
while abs(x) < 80 and abs(y) < 80:
    r = randint(0, 3)
    if r == 0:
        x += 10 # Walk right
        turtle.setheading(0)
        turtle.forward(10)
    elif r == 1:
        y -= 10 # Walk down
        turtle.setheading(270)
        turtle.forward(10)
    elif r == 2:
        x -= 10 # Walk left
        turtle.setheading(90)
        turtle.forward(10)

turtle.done()
