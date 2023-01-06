import random
from turtle import Turtle, Screen
import colorgram

tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)
colors = colorgram.extract("download.jpg", 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_colors = (r, g, b)
    rgb_colors.append(new_colors)

i = 10
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()
tim.showturtle()
tim.speed(50)
number_of_dots = 100
for dot_count in range(1, 101):
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)

my_screen.exitonclick()