# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import *
import random

color_list = [(250, 249, 247), (243, 246, 250), (244, 251, 248), (252, 244, 248), (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40)]

t = Turtle()
t.hideturtle()
t.speed("fastest")

screen = Screen()

t.penup()
t.setposition(-200, 200)
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

for i in range(10):
    for j in range(10):
        t.dot(20, rgb_to_hex(random.choice(color_list)))
        t.forward(50)
    t.backward(50 * 10)
    t.right(90)
    t.forward(50)
    t.left(90)

screen.exitonclick()
