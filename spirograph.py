import random
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


tim.hideturtle()
tim.speed(50)


def draw_spirogrph(size_of_gaps):
    for _ in range(int(360 / size_of_gaps)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gaps)


draw_spirogrph(10)

my_screen.exitonclick()

