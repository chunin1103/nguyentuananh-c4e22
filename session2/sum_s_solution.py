#cach 1:
n = int(input("Nhap so m thich: "))

tong = 0

for i in range(1, n + 1, 1):
    tong += i #tong = tong + i

#cach 2:

r = range(1, n + 1, 1)
s = sum(r)

# ket qua cua 2 cach:

print(tong) 
print(s)