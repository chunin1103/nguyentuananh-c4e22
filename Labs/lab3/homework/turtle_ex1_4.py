from turtle import *

def ex_1():
    print('Hellp World \n' *3)
ex_1()

def ex_2(x, y):
    print(x + y)
ex_2(2, 3)

def draw_square(len_square, color_square):
    color(color_square)
    begin_fill()
    for i in range(4):
        forward(len_square)
        right(90)
    end_fill()

draw_square(100, 'blue')

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()


