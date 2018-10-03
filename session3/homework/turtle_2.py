from turtle import *

shape("square")

x = ["red", "blue", "brown", "yellow", "grey"]

for i in range(5):
    color(x[0 + i])
    begin_fill()

    forward(100)

    for i in range(2): # drawing rectangle
        right(90)
        forward(180)
        right(90)
        forward(100)
    
    end_fill()



mainloop()