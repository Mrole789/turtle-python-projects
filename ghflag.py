from turtle import Turtle, Screen

jon = Turtle()
print(jon)
jon.backward(150)
jon.speed(8)
#jon.shape("turtle")
jon.color("green")

def rec(x):
    """Functiuon for each rectangular colored section of flag."""
    for y in range(25):
        x.forward(300)
        x.left(90)
        x.forward(1)
        x.left(90)
        x.forward(300)
        x.right(90)
        x.forward(1)
        x.right(90)

rec(jon)        
jon.color("yellow")
rec(jon)
jon.color("red")
rec(jon)

jon.penup()
jon.left(90)
jon.backward(1)
jon.right(90)
jon.forward(150)
jon.right(90)
jon.forward(50)
jon.color("black")
jon.right(20)
jon.pendown()

def star(o):
    """Function for sides of the star."""
    for y in range(5):
        o.left(36)
        o.forward(20)
        o.left(180)
        o.right(108)
        o.forward(20)
        o.right(180)

jon.begin_fill()
star(jon)
jon.end_fill()
jon.hideturtle()

ms = Screen()
ms.exitonclick()