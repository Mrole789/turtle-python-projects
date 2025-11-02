from turtle import Turtle, Screen

jon = Turtle()
screen = Screen()

def mf():
    """To move forward"""
    jon.forward(10)
    
def mb():
    """To move backward"""
    jon.backward(10)

def mr():
    """move right"""
    jon.right(10)

def ml():
    """move left"""
    jon.left(10)

def clear():
    """To clear pad"""
    jon.reset()
    
def pu():
    """Penup"""
    jon.penup()
    
def pd():
    """Pendown"""
    jon.pendown()

screen.listen()
screen.onkey(key="w", fun=mf)
screen.onkey(key="z", fun=mb)
screen.onkey(key="a", fun=ml)
screen.onkey(key="s", fun=mr)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=pu)
screen.onkey(key="d", fun=pd)

screen.exitonclick()