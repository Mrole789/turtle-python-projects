from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
u_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]

x = -240 #x-value for .goto()
yv = [75,45,15,-15,-45,-75]
turtles = []

def get_set(t):
    """Gets each turtle ready for the race"""
    global colors, x, yv
    c = random.choice(colors)
    t.penup()
    t.shape("turtle")
    t.color(c)
    y = random.choice(yv)
    t.goto(x,y)
    colors.remove(c)
    yv.remove(y)

for i in range(6):
    new_t = Turtle()
    get_set(new_t)
    turtles.append(new_t)

if u_bet:
    race_on = True
    
while race_on:
    for t in turtles:
        n = random.randint(1,10)
        t.forward(n)
        if t.xcor() >=230:
            winner = t
            race_on = False

if u_bet == winner.color()[0]:
    result = "You won."
else:
    result = "You lost."

print(f"{result} The {winner.color()[0]} turtle won the race.")

screen.exitonclick()