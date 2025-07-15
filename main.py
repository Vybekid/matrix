from turtle import *
from time import sleep

# Set up the screen
bgcolor("black")

# Create two turtle objects to trace the circle's path
t = [Turtle(), Turtle()]
x = 6  # A factor for movement speed
colors = ["lime", "blue", "yellow", "red"]

# Initialize the two turtles
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.penup()
    i.seth(90)     # Face North
    i.forward(350) # Move to the top of the circle
    i.seth(-180)   # Face West
    i.pendown()

# Lift the pen for the first turtle before the main loop
t[0].penup()

# Configure the main turtle (which is invisible) for drawing
delay(0)
speed(0)
hideturtle()
sleep(4) # Pause for 4 seconds before drawing begins

# Main drawing loop
for i in colors:
    color(i)  # Set the color for the current set of lines
    # This loop draws the lines that form the cardioid
    for _ in range(360):
        # Move the first turtle one step
        t[0].forward(x)
        t[0].left(1)
        
        # Move the second turtle two steps (twice the angular speed)
        t[1].forward(2 * x)
        t[1].left(2)
        
        # Draw a line between the positions of the two turtles
        penup()
        goto(t[0].pos())
        pendown()
        goto(t[1].pos())

done()