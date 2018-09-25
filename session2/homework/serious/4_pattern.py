# a

print("here is your initial 20 stars ")
print(20 * "*")

# b

n = int(input("How many more stars to make you happy? "))

print( n * "*")

# c, d

x = int(input("How many MORE x and stars do you want in total? ")) 

for i in range(x):
    if i % 2:
        print("*", end="")
    else:
        print("x", end="")

print()

# e
print("I want to conquer the world", end="")
print()
print("starting with Techkids ((its toilets first))")

# f
n = int(input("enter number of rows (n): "))
m = int(input("enter number of columns (m): "))

for i in range(3):
    print("* " * 5)

