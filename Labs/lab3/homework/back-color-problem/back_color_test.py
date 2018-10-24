from random import *
from turtle import *
import pyautogui

text =[]
color =[]
r = []
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
for i in shapes:
    text.append(i['text'])
for c in shapes:
    color.append(c['color'])

import turtle

# s = []
# def get_mouse_click_coor(x, y):
#     print(x, y)
#     s.append(x)
#     return s, x, y
# onscreenclick(get_mouse_click_coor)
# print(s)

# pos = pyautogui.position()
# x = pos[0]
# y = pos[1]

import turtle

xclick = 0
yclick = 0
x_save = []

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables) # Here's the change!

def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    global x_save
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print(xclick)
    x_save.append(xclick)
    print(yclick)
    print(x_save)
    return [x_save, xclick, rawx, rawy, yclick]
print(x_save)
t = getcoordinates()

print(xclick)

print(text)
print(color)

mainloop()