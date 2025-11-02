import turtle as t
import random

jon = t.Turtle()
t.colormode(255)

def rcolor():
    """Returns a turple of random numbers to be used."""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rc = (r,g,b)
    return rc

d = [90, 180, 270, 360]

jon.speed(10)
jon.width(8)

while 1 > 0:
    jon.pencolor(rcolor())
    jon.forward(20)
    jon.left(random.choice(d))
