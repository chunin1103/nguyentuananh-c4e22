sheepsizes = [5, 7, 300, 90, 24, 50, 75]
totalsize = 0
biggest_size = (max(sheepsizes))
biggest_sheep = sheepsizes.index(biggest_size)
l = len(sheepsizes)

print("Hello, my name is Tuan Anh and here is my flock")
print(sheepsizes, "\n")
print("Now my biggest sheep has size", biggest_size, "let's shear it")
print("After shearing, here is my flock")
sheepsizes.insert(biggest_sheep + 1, 8)
sheepsizes.pop(biggest_sheep)
print(sheepsizes, "\n")

n = int(input("How many months have passed? ",))

for i in range(1, n + 1):

    print("Month", i,":")
    print("One month has passed, now here is my flock")

    pos = 0
    biggest_size = (max(sheepsizes))
    biggest_sheep = sheepsizes.index(biggest_size)

    for _ in range(l):
        sheepsizes[pos]=sheepsizes[pos]+50      # each months my sheeps grow 50 in size
        pos += 1                                # this way or (sheepsizes = [x + 50 for x in sheepsizes])
    print(sheepsizes)
    
    if i < n:
        print("Now my biggest sheep has size", biggest_size, "let's sheer it")
        sheepsizes.insert((biggest_sheep) + 1, 8)
        sheepsizes.pop(biggest_sheep)
        print("After shearing, here is my flock")
        print(sheepsizes, "\n")

for x in sheepsizes:
    totalsize += x 
    
print()
print("My flock has size in total:", totalsize)
total = totalsize * 2
print("I would get", totalsize, "* 2$ =", total, end="$")

