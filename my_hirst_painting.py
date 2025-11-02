import turtle as t
import random

jon = t.Turtle()
t.colormode(255)
jon.speed("fastest")
jon.hideturtle()

def rcolor():
    """Returns a turple of random numbers to be used."""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rc = (r,g,b)
    return rc

#set the turtle to the left end of the window
jon.penup()
jon.right(90)
jon.forward(220)
jon.right(90)
jon.forward(250)
jon.right(180)

def spot():
    """Leaves a spot of color"""
    jon.dot(20, rcolor())
    jon.end_fill()

for x in range(10):
    for x in range(10):
        spot()
        jon.forward(50)
        
    jon.left(90)
    jon.forward(50)
    jon.left(90)
    jon.forward(500)
    jon.right(180)

ms = t.Screen()
ms.exitonclick()