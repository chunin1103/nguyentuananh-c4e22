from eval import evalu # * la import tat ca

x = 5
y = 1
op = input('Op (+, - , *, /): ')

t = evalu(x, y, op)

print(x, op, y, "=", t)