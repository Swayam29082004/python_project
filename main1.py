"""import colorgram
rgb_colors = []
colors = colorgram.extract('20_001.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color =(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
swayam = turtle_module.Turtle()
swayam.speed("fastest")
swayam.penup()
swayam.hideturtle()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),(222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),(64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),(210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),(150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
swayam.setheading(225)
swayam.forward(300)
swayam.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    swayam.dot(20, random.choice(color_list))
    swayam.forward(50)
    if dot_count % 10==0:
        swayam.setheading(90)
        swayam.forward(50)
        swayam.setheading(100)
        swayam.forward(500)
        swayam.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()