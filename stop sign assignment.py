#Matthew Muller
#Stop sign assignment
#CS-175L

import math
import turtle
#Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = 0
TEXT_Y = -(LENGTH / math.sqrt(2)) - 20  

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

t = turtle.Turtle()
t.speed(ANIMATION_SPEED)

t.color("red")

start_x = -(LENGTH / math.sqrt(2))
start_y = LENGTH / 2
t.penup()
t.goto(start_x, start_y)
t.pendown()

for _ in range(NUM_SIDES):
    t.forward(LENGTH)
    t.right(360 / NUM_SIDES)

t.penup()
t.goto(TEXT_X, TEXT_Y)
t.pendown()
t.color("black")
t.write("STOP", align="center", font=("Arial", 24, "normal"))

turtle.mainloop()
