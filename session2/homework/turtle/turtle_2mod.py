from turtle import *

for i in range (3, 7, 1):
    for _ in range (i):
        
        forward(150)
        left(360 / i)

        if i % 2: 
            color("blue")
        else: 
            color("red")        

mainloop()