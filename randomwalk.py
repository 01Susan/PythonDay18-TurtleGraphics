import random
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randoms_color = (r, g, b)
    return randoms_color


direction = [0, 90, 180, 270]
tim.hideturtle()
tim.speed(30)
tim.pensize(15)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


my_screen.exitonclick()
