from turtle import *

#This ex is awesome

speed(0)

def draw_star(x, y, l):
    penup()
    setpos(x, y)
    pendown()
    for i in range(2):
        for _ in range(3):
            right(144)
            forward(l)

color('blue')

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

draw_star(0, 200, 100)


mainloop()
