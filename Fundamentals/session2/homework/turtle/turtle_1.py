from turtle import *

color("red")
speed(0)

for i in range(4):
    for i in range (2):
        left(35)
        forward(100)
        right(35 * 2)
        forward(100)
        right(180 - 35)

    right(90)


mainloop()
