from turtle import *

speed(0)
x = ["red", "blue", "brown", "yellow", "grey"]

for i in range (3, 8, 1):
    color(str(x[i-3]))
    for _ in range(i):
        forward(120)
        left(360 / i)

mainloop()
        
        

    