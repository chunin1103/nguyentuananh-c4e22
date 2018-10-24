from random import *
from turtle import *
text    =[]
color   =[]

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
for t in shapes:
    text.append(t['text'])
for c in shapes:
    color.append(c['color'])
quiz_type = [0, 1] # 0 is meaning, 1 is color

def get_shapes():
    return shapes


def generate_quiz():
    return [
                'RED',
                '#4CAF50',
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    return True
