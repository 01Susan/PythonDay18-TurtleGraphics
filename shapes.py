import random
from turtle import Turtle, Screen

tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen", "SlateGray"]


def shape(times):
    angel = 360 / times
    tim.color(random.choice(colors))
    tim.hideturtle()
    for _ in range(times):
        tim.forward(100)
        tim.right(angel)


for no_of_shape in range(3, 11):
    shape(no_of_shape)

my_screen = Screen()
my_screen.exitonclick()