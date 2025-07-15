from turtle import *
from time import sleep

# Set up the screen
bgcolor("black")

# Create two turtle objects to trace the circle's path
t = [Turtle(), Turtle()]
x = 6  # A factor for movement speed
colors = ["lime", "blue", "yellow", "red"]

for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.penup()
    i.seth(90)     
    i.forward(350) 
    i.seth(-180)  
    i.pendown()

t[0].penup()

delay(0)
speed(0)
hideturtle()
sleep(4) 

for i in colors:
    color(i)  

    for _ in range(360):
        t[0].forward(x)
        t[0].left(1)
        

        t[1].forward(2 * x)
        t[1].left(2)
        
        penup()
        goto(t[0].pos())
        pendown()
        goto(t[1].pos())

done()