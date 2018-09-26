from turtle import *

d = 10

for _ in range(10):
    forward(d)
    d = d + 10 #d += 10
    left(90)

forward(d)   

mainloop()