n = int(input("Enter a number out of curiousity"))

m = 1

for i in range(1, n + 1, 1):
    m *= i
    print(i)

print(m)