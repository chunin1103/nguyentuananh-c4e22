x = ["mun dau den", "mun trung ca", "nam da", "tang nhang"]
n = input("muon xoa gi? ")

# if n.isdigit():
#     x.pop(int(n-1))
#     print(x)
# elif n.isalpha:
#     x.remove(str(n))
#     print(x)
# else:
#     print("There are no such things")

i = input("what to del")
if i.isdigit():
    position = int(i)
    favs.pop(position - 1)
else:
    favs.remove(i)
    
print(i)