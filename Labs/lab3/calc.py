def add(x, y):
    r = x + y
    print(r)
    return r 

a = 5
b = 10
t = add(a , b)
print(t)

def substract(z, c):
    l = z - c
    print(l)
    z += 1
    return z, l + 1

z = 6
c = 5
t = substract(z, c)
print(t)
print(z)
