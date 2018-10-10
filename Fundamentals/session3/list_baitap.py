x = ["agile", "bacon","contra", "dick", "english", "foxtrox"]
print(*x, sep="\n")

n = int(input("Muon xem cai nao? "))

while True:
    if n > len(x):
        print("There are no such things")
        break
    else:
        print(x[n-1])