import eval #.py cai nay goi la module

x = int(input("x = "))
y = int(input("y = "))
# s = x + y

# output = "{0} + {1} = {2}".format(x, y, s)

op = input("Op (+, -, *, /): ")

r = eval.evalu(x, y, op)

print(x, op, y, '=', r)
# output = '{0} + {1} = {2}'.format(x, y, r)
# print(output)