# Turtle is python's built in graphics module for drawing lines, circles, and other shapes, including text. It is easy to learn and simple to use.

# This will draw an Olympic symbol using the Turtle Graphics window.

# I used Windows PowerShell to do this, can't tell you what to use on a Mac :)

# Start off with entering 'python' to jumpstart python access. Enter all these lines one at a time to draw the symbol. A pop up will open once you start.

python

import turtle

turtle.color("blue")

turtle.penup()

turtle.goto(-110, -25)

turtle.pendown()

turtle.circle(45)

turtle.color("black")

turtle.penup()

turtle.goto(0, -25)

turtle.pendown()

turtle.circle(45)

turtle.color("red")

turtle.penup()

turtle.goto(110, -25)

turtle.pendown()

turtle.circle(45)

turtle.color("yellow")

turtle.penup()

turtle.goto(-55, -75)

turtle.pendown()

turtle.circle(45)

turtle.color("green")

turtle.penup()

turtle.goto(55, -75)

turtle.pendown()

turtle.circle(45)

turtle.done()
