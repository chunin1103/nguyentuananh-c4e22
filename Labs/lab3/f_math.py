from random import randint, choice
from eval import *

def generate_quiz():
    x = randint(0, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    error = randint(-1, 1)
    
    r = evalu(x, y, op) + error
    
    return [x, y, op, r, error]

x, y, op, r, error = generate_quiz()
# quiz = generate_quiz()
# x = quiz[0]
# y = quiz[1]
# op= quiz[2]
# r = quiz[3]
# error = quiz[4]

output = '{0} {3} {1} = {2}'.format(x, y, r, op)
print(output)

user_answer = input("(Y/N)? ").upper()

# if r == x (+-*/) y
if r == evalu(x, y, op):
    if user_answer == "Y":
        print("Yay you")
    else:
        print("Stay in school, kid")
    
else:
    if user_answer == "Y":
        print("Stay in school, kid")
    else:
        print('Yay')
