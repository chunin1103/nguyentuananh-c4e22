from turtle import *

speed(3)

# x,y axis
setpos(300, 0)
home()
setpos(0,-400)
home()

def is_inside(point, rec):
    
    # point
    penup()
    setpos(point[0],-point[1])
    pendown()
    color('dodger blue')
    dot()
    
    #rectangle
    penup()
    setpos(rec[0],-rec[1])
    pendown()
    color("#cc221a")
    begin_fill()
    for i in range(2):
        forward(rec[2])
        right(90)
        forward(rec[3])
        right(90)
    end_fill()

    # check
    if rec[0] < point[0] < rec[2] + rec[0] and rec[1] < point[1] < rec[3] + rec[1]:
        return True
    else:
        return False

point = [200, 120]
rec   = [140, 60, 100, 200]
check = is_inside(point, rec)
print(check)

mainloop()