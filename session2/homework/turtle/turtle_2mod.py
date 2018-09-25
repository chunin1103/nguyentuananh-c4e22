from turtle import *

# sides 
# left (goc)
# gpc = 360 / sides 

sides = 3


# for i in range (10):
#     for i in range(sides):
#         if sides <= 5:

#                 forward(100)
#                 left(360 / sides)
            
#     sides = sides + 1

for i in range (3, 7, 1):
    for _ in range (i):
        
        forward(300)
        left(360 / i)

        if i % 2: 
            color("blue")
        else: 
            color("red")        

mainloop()